import pyglet

# bg image
screen1 = pyglet.resource.image('assets/screen1.png')

## bg position
screen1_sprite = pyglet.sprite.Sprite(screen1)
screen1_sprite.scale = 0.85
screen1_sprite.position = (0, 0)

# buttons
continue_btn = pyglet.resource.image('assets/continue.png')
continue_btn_click = pyglet.resource.image('assets/continue-click.png')

openfile1_btn = pyglet.resource.image('assets/openfile1.png')
openfile1_btn_click = pyglet.resource.image('assets/openfile1-click.png')

openfile2_btn = pyglet.resource.image('assets/openfile2.png')
openfile2_btn_click = pyglet.resource.image('assets/openfile2-click.png')
openfile2_btn_na = pyglet.resource.image('assets/openfile2-na.png')

openfileloc_btn = pyglet.resource.image('assets/openfileloc.png')
openfileloc_btn_click = pyglet.resource.image('assets/openfileloc-click.png')
openfileloc_btn_na = pyglet.resource.image('assets/openfileloc-na.png')

## button positions
continue_btn_sprite = pyglet.sprite.Sprite(continue_btn)
continue_btn_sprite.scale = 0.17
continue_btn_sprite.position = (686, 50)

continue_btnclick_sprite = pyglet.sprite.Sprite(continue_btn_click)
continue_btnclick_sprite.scale = 0.17
continue_btnclick_sprite.position = (686, 50)

openfile1_btn_sprite = pyglet.sprite.Sprite(openfile1_btn)
openfile1_btn_sprite.scale = 0.14
openfile1_btn_sprite.position = (361, 595)

openfile1_btnclick_sprite = pyglet.sprite.Sprite(openfile1_btn_click)
openfile1_btnclick_sprite.scale = 0.14
openfile1_btnclick_sprite.position = (361, 595)

openfile2_btn_sprite = pyglet.sprite.Sprite(openfile2_btn)
openfile2_btn_sprite.scale = 0.14
openfile2_btn_sprite.position = (361, 185)

openfile2_btnclick_sprite = pyglet.sprite.Sprite(openfile2_btn_click)
openfile2_btnclick_sprite.scale = 0.14
openfile2_btnclick_sprite.position = (361, 185)

openfile2_btnna_sprite = pyglet.sprite.Sprite(openfile2_btn_na)
openfile2_btnna_sprite.scale = 0.14
openfile2_btnna_sprite.position = (361, 185)

openfileloc_btn_sprite = pyglet.sprite.Sprite(openfileloc_btn)
openfileloc_btn_sprite.scale = 0.19
openfileloc_btn_sprite.position = (361, 390)

openfileloc_btnclick_sprite = pyglet.sprite.Sprite(openfileloc_btn_click)
openfileloc_btnclick_sprite.scale = 0.19
openfileloc_btnclick_sprite.position = (361, 390)

openfileloc_btnna_sprite = pyglet.sprite.Sprite(openfileloc_btn_na)
openfileloc_btnna_sprite.scale = 0.19
openfileloc_btnna_sprite.position = (361, 390)