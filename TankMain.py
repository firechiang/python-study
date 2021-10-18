'''
坦克大战游戏（注意：需要安装pygame模块：pip install pygame）
'''
import sys

import sys,pygame,time,random

# 图像
class Item(pygame.sprite.Sprite):
    def __init__(self,surface):
        pygame.sprite.Sprite.__init__(self)
        # 窗口画布
        self.surface = surface

# 坦克
class Tank(Item):
    # 坦克宽度和高度
    witch = 50
    height = 50

    def __init__(self,surface,left,top):
        super(Tank, self).__init__(surface)
        # 坦克是否停止
        self.stop = True
        # 坦克移动的速度
        self.speed = 8
        # 坦克方向（默认向下） U 上，D 下 ，L 左 ，R 右
        self.direction = "U"
        # 坦克的所有图片(以方向为KEY)
        self.images = {
            "U":pygame.image.load("tank_images/tankU.gif"),
            "D":pygame.image.load("tank_images/tankD.gif"),
            "L":pygame.image.load("tank_images/tankL.gif"),
            "R":pygame.image.load("tank_images/tankR.gif")
        }
        # 坦克
        self.image = self.images[self.direction]
        # 坦克所在位置
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        # 坦克是否存在
        self.live = True

    # 显示坦克（将坦克画到窗口上）
    def show(self):
        # 坦克
        self.image = self.images[self.direction]
        # 将坦克画到窗口上
        self.surface.blit(self.image,self.rect)

    # 移动坦克
    def move(self):
        # 如果坦克不是停止状态
        if not self.stop:
            if self.direction == "L":
                if self.rect.left > 0:
                    self.rect.left -=self.speed
                else:
                    self.left = 0

            if self.direction == "R":
                if self.rect.right < TankMain.width:
                    self.rect.right+=self.speed
                else:
                    self.rect.right = TankMain.width

            if self.direction == "U":
                if self.rect.top > 0:
                    self.rect.top -= self.speed
                else:
                    self.rect.top = 0

            if self.direction == "D":
                if self.rect.bottom < TankMain.height:
                    self.rect.bottom+=self.speed
                else:
                    self.rect.bottom = TankMain.height

    # 开炮
    def fire(self):
        return Mis(self.surface,self)

# 爆炸
class Blast(Item):
    width = 50
    height = 50

    def __init__(self,surface,left,top):
        super(Blast, self).__init__(surface)
        self.size = 10
        self.max = False
        self.index = 0
        self.images = {
            0:pygame.image.load("tank_images/10.gif"),
            1: pygame.image.load("tank_images/10.gif"),
            2: pygame.image.load("tank_images/10.gif"),
            3: pygame.image.load("tank_images/10.gif"),
            4: pygame.image.load("tank_images/10.gif"),
            5: pygame.image.load("tank_images/10.gif"),
            6: pygame.image.load("tank_images/10.gif"),
            7: pygame.image.load("tank_images/10.gif"),
            8: pygame.image.load("tank_images/10.gif"),
            9: pygame.image.load("tank_images/10.gif"),
            10: pygame.image.load("tank_images/10.gif")
        }
        # 爆炸图片
        self.image = self.images[self.index]
        # 爆炸所在位置
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        # 爆炸是否存在
        self.live = True

    # 爆炸变化，由小变大，由大变小
    def change(self):
        if not self.max:
            self.index += 1
            if self.index == 10:
                self.max = True
        else:
            self.index -= 1
            if self.index == 0:
                self.live = False

    # 显示爆炸（将爆炸画到窗口上）
    def show(self):
        if(self.live):
            # 爆炸
            self.image = self.images[self.index]
            # 将爆炸画到窗口上
            self.surface.blit(self.image,self.rect)

# 炮弹
class Mis(Item):
    # 宽度和高度
    witch = 12
    height = 12

    def __init__(self,surface,tank):
        super(Mis, self).__init__(surface)
        self.tank = tank
        # 炮弹是否停止
        self.stop = True
        # 炮弹动的速度
        self.speed = 10
        # 炮弹方向（等于坦克的方向） U 上，D 下 ，L 左 ，R 右
        self.direction = tank.direction
        # 炮弹的所有图片(以方向为KEY)
        self.images = {
            "U":pygame.image.load("tank_images/missileU.gif"),
            "D":pygame.image.load("tank_images/missileD.gif"),
            "L":pygame.image.load("tank_images/missileL.gif"),
            "R":pygame.image.load("tank_images/missileR.gif")
        }
        # 炮弹
        self.image = self.images[self.direction]
        # 炮弹所在位置
        self.rect = self.image.get_rect()
        # 双杠表示取整
        self.rect.left = tank.rect.left + (tank.witch - Mis.witch) // 2
        self.rect.top = tank.rect.top + (tank.height - Mis.height) // 2
        # 炮弹是否存在
        self.live = True

    # 显示炮弹（将炮弹画到窗口上）
    def show(self):
        if(self.live):
            # 炮弹
            self.image = self.images[self.direction]
            # 将炮弹画到窗口上
            self.surface.blit(self.image,self.rect)


    # 移动炮弹
    def move(self):
        # 如果炮弹还存在
        if self.live:
            if self.direction == "L":
                if self.rect.left > 0:
                    self.rect.left -=self.speed
                else:
                    self.live = False

            if self.direction == "R":
                if self.rect.right < TankMain.width:
                    self.rect.right+=self.speed
                else:
                    self.live = False

            if self.direction == "U":
                if self.rect.top > 0:
                    self.rect.top -= self.speed
                else:
                    self.live = False

            if self.direction == "D":
                if self.rect.bottom < TankMain.height:
                    self.rect.bottom+=self.speed
                else:
                    self.live = False
    # 碰撞坦克
    def collision(self):
        for tank in TankMain.enemy_list:
            if self.direction == "U":
                if self.rect.top >= tank.rect.bottom and self.rect.top <= tank.rect.top:
                    tank.live = False
                    TankMain.enemy_list.remove(tank)


# 墙
class Wall(Item):
    pass

# 我方坦克
class MyTank(Tank):
    def __init__(self,surface):
        super(MyTank, self).__init__(surface,400,600)





# 敌方坦克
class EnemyTabk(Tank):

    def __init__(self,surface):
        super(EnemyTabk, self).__init__(surface,random.randint(1,5)*100,200)
        # 生成随机方向或停止
        self.random_direction()

    # 生成随机方向或停止
    def random_direction(self):
        # 坦克固定移动步数才转变方向或停止
        self.step = 10
        # 坦克是否停止
        self.stop = False
        r = random.randint(0,4)
        # 随机坦克的方向
        if r == 0:
            self.stop = True
        elif r == 1:
            self.direction = "L"
        elif r == 2:
            self.direction = "R"
        elif r == 3:
            self.direction = "U"
        elif r == 4:
            self.direction = "D"

    # 随机移动
    def random_move(self):
        # 如果坦克还活着
        if self.live:
            # 固定步数移动完成或者坦克是停止的
            if self.step == 0 or self.stop == True:
                # 生成随机方向或停止
                self.random_direction()
            # 向固定方向移动
            else:
                self.move()
                # 坦克固定移动步数减1
                self.step-=1



# Tank游戏主界面
class TankMain(object):
    # 窗口宽高
    width = 800
    height = 700

    # 炮弹集合
    mis_list = []
    # 敌方坦克集合
    enemy_list = []

    # 开始游戏
    def start(self):
        # 初始化pygame模块
        pygame.init()
        # 创建一个窗口
        # 第一个参数是大小,第二个参数 是否可改变窗口大小
        surface = pygame.display.set_mode((TankMain.width,TankMain.height),0,32)
        # 设置窗口名称
        pygame.display.set_caption("坦克大战")
        # 创建我方坦克
        my_tank = MyTank(surface)

        for i in range(1,6):
            TankMain.enemy_list.append(EnemyTabk(surface))


        while True:
            # 设置窗口背景色
            # 第一个参数是颜色 color RGB(0,0,0)
            surface.fill((0,0,0))
            # 在屏幕的左上角画文字（第二个参数文字要画的位置）
            surface.blit(self.write_text(),(0,5))
            # 显示我方坦克
            my_tank.show()
            # 移动我方坦克
            my_tank.move()

            # 炮弹
            for mis in TankMain.mis_list:
                # 炮弹还存在
                if mis.live:
                    # 显示炮弹
                    mis.show()
                    # 碰撞坦克
                    mis.collision()
                    # 移动炮弹
                    mis.move()
                # 炮弹不在了删除
                else:
                    TankMain.mis_list.remove(mis)

            # 敌方坦克
            for enemy_t in TankMain.enemy_list:
                # 显示敌方坦克
                enemy_t.show()
                # 随机移动敌方坦克
                enemy_t.random_move()

            # 事件处理
            self.event_handler(my_tank)
            # 线程睡眠 0.003秒
            time.sleep(0.03)
            # 显示重置
            pygame.display.update()
    # 关闭游戏
    def stop(self):
        # 退出程序
        sys.exit()

    def setTital(self):
        pass

    # 在屏幕的左上角显示文字
    def write_text(self):
        # 第一个参数是字体名称（可使用 pygame.font.get_fonts() 获取到系统里面所有的文字格式）
        font = pygame.font.SysFont("cn",20)
        text_sf = font.render(f"敌方坦克数量: {len(TankMain.enemy_list)},炮弹数量: {len(TankMain.mis_list)}", True, (255, 255, 255))
        return text_sf

    # 事件处理器
    def event_handler(self,my_tank):
        for event in pygame.event.get():
            # 关闭窗口事件
            if event.type == pygame.QUIT:
                self.stop()
                break
            # 键盘按下事件
            if event.type == pygame.KEYDOWN:
                # 左
                if event.key == pygame.K_LEFT:
                    my_tank.direction = "L"
                    my_tank.stop = False
                # 右
                if event.key == pygame.K_RIGHT:
                    my_tank.direction = "R"
                    my_tank.stop = False
                # 上
                if event.key == pygame.K_UP:
                    my_tank.direction = "U"
                    my_tank.stop = False
                # 下
                if event.key == pygame.K_DOWN:
                    my_tank.direction = "D"
                    my_tank.stop = False

                # 按下Esc键(程序退出)
                if event.key == pygame.K_ESCAPE:
                    self.stop()

                # 按下空格发射炮弹
                if event.key == pygame.K_SPACE:
                    # 将炮弹放入集合
                    TankMain.mis_list.append(my_tank.fire())

            # 键盘弹起事件
            if event.type == pygame.KEYUP:
                # 键盘弹起坦克停止移动
                if (event.key == pygame.K_LEFT and my_tank.direction == "L") or (event.key == pygame.K_RIGHT and my_tank.direction == "R") or \
                        (event.key == pygame.K_UP and my_tank.direction == "U") or (event.key == pygame.K_DOWN and my_tank.direction == "D"):
                    my_tank.stop = True




if __name__ == "__main__":
    game = TankMain()
    game.start()
