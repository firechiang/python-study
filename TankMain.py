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
        # 记录坦克之前的位置
        self.oldtop = self.rect.top
        self.oldleft = self.rect.left
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
            # 记录坦克原来的位置
            self.oldtop = self.rect.top
            self.oldleft = self.rect.left
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

    # 坦克还原到原来的位置
    def reduction(self):
        self.rect.top = self.oldtop
        self.rect.left = self.oldleft

# 爆炸
class Blast(Item):
    width = 50
    height = 50

    def __init__(self,surface,rect):
        super(Blast, self).__init__(surface)
        #self.size = 10
        #self.max = False
        #self.index = 0
        self.images = [pygame.image.load("tank_images/0.gif"),\
                       pygame.image.load("tank_images/1.gif"),\
                       pygame.image.load("tank_images/2.gif"),\
                       pygame.image.load("tank_images/3.gif"),\
                       pygame.image.load("tank_images/4.gif"),\
                       pygame.image.load("tank_images/5.gif"),\
                       pygame.image.load("tank_images/6.gif"),\
                       pygame.image.load("tank_images/7.gif"),\
                       pygame.image.load("tank_images/8.gif"),\
                       pygame.image.load("tank_images/9.gif"),\
                       pygame.image.load("tank_images/10.gif")]
        # 爆炸图片
        #self.image = self.images[self.index]
        # 爆炸所在位置
        #self.rect = self.image.get_rect()
        #self.rect.left = left
        #self.rect.top = top
        # 爆炸是否存在
        self.live = True
        # 爆炸图片位置
        self.step = 0
        # 爆炸显示的位置（默认传过来的位置就是坦克的位置）
        self.rect = rect

    # 爆炸显示函数
    def display(self):
        # 爆炸是否还存活
        if self.live:
            # 如果爆炸图片已显示到最后一张图片了
            if self.step == len(self.images):
                self.live = False
            else:
                self.image = self.images[self.step]
                # 将炮弹画到窗口上
                self.surface.blit(self.image, self.rect)
                # 爆炸放大
                self.step += 1
        else:
            TankMain.balst_list.remove(self)

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
        # 炮弹好坏: 敌方坦克炮弹 False，我方坦克炮弹 True
        self.good = False

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
        # 我方坦克发射的炮弹
        if self.good:
            # 是否碰撞（最后一个参数表示是否要删除已碰撞的元素）
            collision_list = pygame.sprite.spritecollide(self,TankMain.enemy_list,False)
            # 循环已碰撞的元素
            for t in collision_list:
                # 敌方坦克没了
                t.live = False
                # 炮弹也没了
                self.live = False
                # 初始化爆炸
                balst = Blast(self.surface,t.rect)
                # 将炮弹加入集合
                TankMain.balst_list.append(balst)


# 墙
class Wall(Item):
    def __init__(self, surface, left, top, width, height):
        super(Wall, self).__init__(surface)
        self.rect = pygame.Rect(left, top, width, height)
        self.color = (255,0,0)

    def display(self):
        # 画墙
        self.surface.fill(self.color,self.rect)

    # 墙和坦克的碰撞检测
    def hit_other(self):
        # 我方坦克与墙碰撞
        if TankMain.my_tank:
            is_hit = pygame.sprite.collide_rect(self,TankMain.my_tank)
            # 问题：碰撞后让坦克停止，但是坦克此时已经碰撞，将无法移动
            # 解决方案：如果能知道坦克是哪个方向撞墙了，就让那一个方向停止即可解决上述问题
            if is_hit:
                TankMain.my_tank.stop = True
                # 坦克与墙碰撞后，让坦克回到之前的位置
                TankMain.my_tank.reduction()
# 我方坦克
class MyTank(Tank):
    def __init__(self,surface):
        self.live = True
        super(MyTank, self).__init__(surface,400,600)

    # 我方坦克碰撞敌方子弹
    def collect_mis(self):
        m_list = pygame.sprite.spritecollide(self,TankMain.mis_list,False)
        for m in m_list:
            if not m.good:
                m.live = False
                TankMain.mis_list.remove(m)
                self.live = False
                # 初始化爆炸
                balst = Blast(self.surface, self.rect)
                # 将炸弹加入集合
                TankMain.balst_list.append(balst)
                break;


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
    # 随机开炮
    def random_k(self):
        r = random.randint(0,50)
        if r > 40:
            # 初始化炮弹
            m = self.fire()
            TankMain.mis_list.add(m)
        else:
            pass


# Tank游戏主界面
class TankMain(object):
    # 窗口宽高
    width = 800
    height = 700

    # 我方坦克
    my_tank = None
    # 炮弹集合
    mis_list = pygame.sprite.Group()
    # 敌方坦克集合
    enemy_list = pygame.sprite.Group()
    # 炸弹集合
    balst_list = []
    # 墙
    wall = None

    # 开始游戏
    def start(self):
        # 初始化pygame模块
        pygame.init()
        # 创建一个窗口
        # 第一个参数是大小,第二个参数 是否可改变窗口大小
        surface = pygame.display.set_mode((TankMain.width,TankMain.height),0,32)
        # 设置窗口名称
        pygame.display.set_caption("坦克大战")
        # 创建墙
        TankMain.wall = Wall(surface,100,200,100,20)
        # 创建我方坦克
        TankMain.my_tank = MyTank(surface)
        # 初始化敌方坦克
        for i in range(1,6):
            TankMain.enemy_list.add(EnemyTabk(surface))


        while True:
            # 设置窗口背景色
            # 第一个参数是颜色 color RGB(0,0,0)
            surface.fill((0,0,0))
            # 在屏幕的左上角画文字（第二个参数文字要画的位置）
            surface.blit(self.write_text(),(0,5))
            # 显示墙
            TankMain.wall.display()
            # 墙与坦克碰撞检测
            TankMain.wall.hit_other()
            # 显示我方坦克
            if TankMain.my_tank.live:
                # 我方坦克与敌方子弹做碰撞检测
                TankMain.my_tank.collect_mis()
                # 显示我方坦克
                TankMain.my_tank.show()
                # 移动我方坦克
                TankMain.my_tank.move()
            else:
                print("游戏结束")
                #sys.exit()
                #del(my_tank)
                #my_tank = None

            # 显示炮弹
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

            # 显示敌方坦克
            for enemy_t in TankMain.enemy_list:
                if enemy_t.live:
                    # 显示敌方坦克
                    enemy_t.show()
                    # 随机移动敌方坦克
                    enemy_t.random_move()
                    # 随机开炮
                    enemy_t.random_k()
                else:
                    TankMain.enemy_list.remove(enemy_t)

            # 显示爆炸
            for blast in TankMain.balst_list:
                blast.display()

            # 事件处理
            self.event_handler(TankMain.my_tank)
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
                    # 构建炮弹
                    my_mis = my_tank.fire()
                    # 我方坦克发射的炮弹
                    my_mis.good = True
                    # 将炮弹放入集合
                    TankMain.mis_list.add(my_mis)

            # 键盘弹起事件
            if event.type == pygame.KEYUP:
                # 键盘弹起坦克停止移动
                if (event.key == pygame.K_LEFT and my_tank.direction == "L") or (event.key == pygame.K_RIGHT and my_tank.direction == "R") or \
                        (event.key == pygame.K_UP and my_tank.direction == "U") or (event.key == pygame.K_DOWN and my_tank.direction == "D"):
                    my_tank.stop = True




if __name__ == "__main__":
    game = TankMain()
    game.start()
