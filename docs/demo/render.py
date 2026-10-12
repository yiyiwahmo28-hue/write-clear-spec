"""Render the README's editorial replay from its public storyboard.

Optional asset-authoring dependency: Pillow. This is not part of the skill runtime.
Usage: python docs/demo/render.py --font font.ttc --bold-font bold-font.ttc
The font must support Chinese and Latin characters.
"""
import argparse
from functools import lru_cache
import json
from pathlib import Path
import re

from PIL import Image, ImageColor, ImageDraw, ImageFont

BASE = Path(__file__).resolve().parent
ASSETS = BASE.parent / 'assets'
WIDTH, HEIGHT, SCALE = 1200, 640, 2
COLORS = dict(ink='#172B4D', muted='#5D6C84', blue='#1677FF', pale='#EEF5FF',
              orange='#B9650E', orange_bg='#FFF5E8', line='#E1E9F5')


def render_scene(data, scene, index, regular_path, bold_path):
    canvas = Image.new('RGB', (WIDTH*SCALE, HEIGHT*SCALE), '#F1F5FC')
    draw = ImageDraw.Draw(canvas)

    @lru_cache(maxsize=32)
    def font(size, bold=False):
        return ImageFont.truetype(str(bold_path if bold else regular_path), size*SCALE)

    def rect(box, fill, radius=0, outline=None):
        draw.rounded_rectangle(tuple(round(v*SCALE) for v in box), radius=radius*SCALE,
                               fill=fill, outline=outline, width=SCALE)

    def text(x, y, value, size=24, fill=None, bold=False):
        draw.text((x*SCALE,y*SCALE),value,font=font(size,bold),fill=fill or COLORS['ink'],anchor='lt')

    def wrap(value, size, max_width, bold=False):
        lines=[]
        for paragraph in value.split('\n'):
            tokens = list(paragraph) if re.search('[\u3400-\u9fff]',paragraph) else re.findall(r'\S+\s*',paragraph)
            line=''
            for token in tokens:
                candidate=line+token
                if line and font(size,bold).getlength(candidate)/SCALE > max_width:
                    lines.append(line.rstrip()); line=token.lstrip()
                else:
                    line=candidate
            lines.append(line.rstrip())
        return lines

    def paragraph(x, y, value, size=24, width=640, fill=None, bold=False, leading=1.42):
        lines=wrap(value,size,width,bold)
        for i,line in enumerate(lines):
            text(x,y+i*size*leading,line,size,fill,bold)
        return y+len(lines)*size*leading

    rect((24,20,1176,624),'#DCE5F3',22)
    rect((24,16,1176,620),'white',22)
    rect((54,39,87,76),COLORS['blue'],8)
    for i,w in enumerate((18,14,10)):
        rect((62,47+i*8,62+w,50+i*8),'white',1)
    text(100,47,'write-clear-spec',20,bold=True)
    text(976,48,data['badge'],15,COLORS['muted'])
    rect((54,90,1146,91),COLORS['line'])
    assert len(wrap(scene['headline'],34,1090,True)) == 1, scene['headline']
    text(55,110,scene['headline'],34,bold=True)

    for i,label in enumerate(data['steps']):
        x=56+i*220
        active=i==index
        rect((x,168,x+28,196),COLORS['blue'] if active else '#EAF0F8',14)
        text(x+8,174,str(i+1),14,'white' if active else COLORS['muted'],True)
        text(x+38,173,label,17,COLORS['blue'] if active else COLORS['muted'],active)

    rect((54,220,402,543),COLORS['pale'],16)
    text(78,242,scene['left_label'],17,COLORS['blue'],True)
    end=paragraph(78,282,scene['left'],26,300,bold=True,leading=1.55)
    assert end <= 457, (scene['left'],end)
    if scene.get('left_note'):
        end=paragraph(78,466,scene['left_note'],17,298,COLORS['muted'],leading=1.4)
        assert end <= 535, (scene['left_note'],end)

    for row_index,row in enumerate(scene['rows']):
        top=226+row_index*105
        is_open=row.get('open',False)
        accent=COLORS['orange'] if is_open else COLORS['blue']
        bg=COLORS['orange_bg'] if is_open else '#F7F9FD'
        rect((427,top,1146,top+94),bg,12)
        rect((445,top+18,479,top+52),accent,10)
        text(457,top+25,'?' if is_open else str(row_index+1),18,'white',True)
        end=paragraph(497,top+15,row['title'],25,628,bold=True,leading=1.18)
        assert end <= top+49, (row['title'],end)
        end=paragraph(497,top+54,row['body'],19,628,COLORS['muted'],leading=1.3)
        assert end <= top+88, (row['body'],end)

    text(55,566,data['disclosure'],15,COLORS['muted'])
    text(1053,566,f'{index+1:02d} / 05',15,COLORS['muted'])
    for i in range(5):
        x=55+i*220
        rect((x,596,x+207,600),COLORS['blue'] if i<=index else '#EAF0F8',2)
    return canvas.resize((WIDTH,HEIGHT),Image.Resampling.LANCZOS)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--font',type=Path,required=True)
    parser.add_argument('--bold-font',type=Path,required=True)
    parser.add_argument('--contact-dir',type=Path)
    args=parser.parse_args()
    story=json.loads((BASE/'storyboard.json').read_text(encoding='utf-8'))
    ASSETS.mkdir(exist_ok=True)
    for lang,data in story['languages'].items():
        scenes=[render_scene(data,s,i,args.font,args.bold_font) for i,s in enumerate(data['scenes'])]
        # The poster makes the consequential rule change visible without animation.
        scenes[-1].save(ASSETS/f'demo-{lang}.png',optimize=True)
        strip=Image.new('RGB',(WIDTH,HEIGHT*len(scenes)))
        for i,scene in enumerate(scenes): strip.paste(scene,(0,i*HEIGHT))
        palette=strip.resize((600,1600)).quantize(colors=240,method=Image.Quantize.MEDIANCUT)
        # Reserve flat colors alongside the sampled antialiasing shades.
        fixed=['#FFFFFF','#F1F5FC','#DCE5F3','#1677FF','#EEF5FF','#F7F9FD',
               '#FFF5E8','#172B4D','#5D6C84','#B9650E','#E1E9F5','#EAF0F8']
        fixed += ['#FFFFFF']*(16-len(fixed))
        palette.putpalette(palette.getpalette()[:720]+[c for color in fixed for c in ImageColor.getrgb(color)])
        frames=[]; durations=[]
        for i,scene in enumerate(scenes):
            frames.append(scene.quantize(palette=palette,dither=Image.Dither.NONE))
            durations.append(data['scenes'][i]['duration_ms'])
            # Short dissolves, followed by long still holds for reading.
            following=scenes[(i+1)%len(scenes)]
            for amount in (0.25,0.5,0.75):
                frames.append(Image.blend(scene,following,amount).quantize(palette=palette,dither=Image.Dither.NONE))
                durations.append(60)
        path=ASSETS/f'demo-{lang}.gif'
        frames[0].save(path,save_all=True,append_images=frames[1:],duration=durations,
                       loop=0,optimize=True,disposal=1)
        with Image.open(path) as check:
            assert check.size == (WIDTH,HEIGHT)
            assert check.n_frames == len(frames)
            actual_duration=0
            for i in range(check.n_frames):
                check.seek(i); actual_duration+=check.info.get('duration',0)
            assert actual_duration == sum(durations)
        if args.contact_dir:
            args.contact_dir.mkdir(parents=True,exist_ok=True)
            strip.resize((720,1920),Image.Resampling.LANCZOS).save(args.contact_dir/f'demo-contact-{lang}.png')
            for i,scene in enumerate(scenes): scene.save(args.contact_dir/f'{lang}-{i+1:02d}.png')
        print(json.dumps({'language':lang,'frames':len(frames),'duration_ms':sum(durations),
                          'dimensions':[WIDTH,HEIGHT],'gif_bytes':path.stat().st_size}))


if __name__ == '__main__':
    main()
