import pyglet

# bg image
screen2 = pyglet.resource.image('assets/screen2.png')


## bg position
screen2_sprite = pyglet.sprite.Sprite(screen2)
screen2_sprite.scale = 0.85
screen2_sprite.position = (0, 0)


# buttons
input_btn = pyglet.resource.image('assets/inputfirsttimer.png')
input_btn_click = pyglet.resource.image('assets/inputfirsttimer-click.png')
input_btn_na = pyglet.resource.image('assets/inputfirsttimer-na.png')

opencam_btn = pyglet.resource.image('assets/opencam.png')
opencam_btn_click = pyglet.resource.image('assets/opencam-click.png')

exit_btn = pyglet.resource.image('assets/exit.png')
exit_btn_click = pyglet.resource.image('assets/exit-click.png')
exit_btn_na = pyglet.resource.image('assets/exit-na.png')

closecam = pyglet.resource.image('assets/closecam.png')

## button positions
input_btn_sprite = pyglet.sprite.Sprite(input_btn)
input_btn_sprite.scale = 0.12
input_btn_sprite.position = (45,175)

input_btnclick_sprite = pyglet.sprite.Sprite(input_btn_click)
input_btnclick_sprite.scale = 0.12
input_btnclick_sprite.position = (45, 175)

input_btnna_sprite = pyglet.sprite.Sprite(input_btn_na)
input_btnna_sprite.scale = 0.12
input_btnna_sprite.position = (45, 175)

exit_btn_sprite = pyglet.sprite.Sprite(exit_btn)
exit_btn_sprite.scale = 0.12
exit_btn_sprite.position = (45, 35)

exit_btnclick_sprite = pyglet.sprite.Sprite(exit_btn_click)
exit_btnclick_sprite.scale = 0.12
exit_btnclick_sprite.position = (45, 35)

exit_btnna_sprite = pyglet.sprite.Sprite(exit_btn_na)
exit_btnna_sprite.scale = 0.12
exit_btnna_sprite.position = (45, 35)

opencam_btn_sprite = pyglet.sprite.Sprite(opencam_btn)
opencam_btn_sprite.scale = 0.12
opencam_btn_sprite.position = (45, 315)

opencam_btnclick_sprite = pyglet.sprite.Sprite(opencam_btn_click)
opencam_btnclick_sprite.scale = 0.12
opencam_btnclick_sprite.position = (45, 315)

closecam_sprite = pyglet.sprite.Sprite(closecam)
closecam_sprite.scale = 0.2
closecam_sprite.position = (55, 430)