import pyglet

# bg image
screen4 = pyglet.resource.image('assets/screen4.png')

## bg position
screen4_sprite = pyglet.sprite.Sprite(screen4)
screen4_sprite.scale = 0.85
screen4_sprite.position = (0, 0)

# buttons
return_btn = pyglet.resource.image('assets/return.png')
return_btn_click = pyglet.resource.image('assets/return-click.png')

# button positions
return_btn_sprite = pyglet.sprite.Sprite(return_btn)
return_btn_sprite.scale = 0.17
return_btn_sprite.position = (660, 50)

return_btnclick_sprite = pyglet.sprite.Sprite(return_btn_click)
return_btnclick_sprite.scale = 0.17
return_btnclick_sprite.position = (660, 50)