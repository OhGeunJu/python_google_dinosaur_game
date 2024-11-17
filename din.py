import pygame
import sys
 
#step 0 : 시작 전 설치된 파이썬 환경에 pygame을 설치해 주어야 합니다. (명령어 : pip install pygame)
#step 1 : 게임 화면 설정
#step 2 : 공룡, 나무 객체 생성
#step 3 : 게임 시작(반복문)
#  step 3-1 : 버튼 클릭 이벤트 처리
#  step 3-2 : 공룡 및 나무 좌표 이동
#  step 3-3 : 화면 갱신
#  step 3-4 : 충돌 발생시 반복 문 탈출
#step 4 : 게임 종료
#Pygame 한국어 doc : https://runebook.dev/ko/docs/pygame/-index-
#Pygame 원문 doc : https://www.pygame.org/docs/


pygame.init() # 게임 초기화
pygame.display.set_caption('python game') # 게임 타이틀
MAX_WIDTH = 800 # 화면 크기
MAX_HEIGHT = 400
 
def main():
    #게임 화면 설정
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    fps = pygame.time.Clock()
 
    #공룡 객체
    Dino = pygame.image.load('c:/텀프로~2/공룡 게임_예제/images/dino0.png')
    Dino_height = Dino.get_size()[1]
    Dino_bottom = MAX_HEIGHT - Dino_height
    dino_pos_x = 50
    dino_pos_y = Dino_bottom
    jump_max = 200
    landing = True
    jump = False

    #나무 객체
    Tree = pygame.image.load('c:/텀프로~2/공룡 게임_예제/images/tree1.png')
    tree_height = Tree.get_size()[1]
    tree_x = MAX_WIDTH
    tree_y = MAX_HEIGHT - tree_height
    tree_speed = 12

    Score = 0
    second = 1
    file = open("Score.txt", 'a')

    #게임 시작 대기 화면
    SB = 0
    while SB == 0:
        fps.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:                   
                    SB = 1
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0, 0, 0))
        font = pygame.font.Font("C:/Windows/Fonts/12롯데마트드림Bold.ttf", 15)
        text_start = font.render("Space 키로 게임을 시작해주세요.", True, (255,255,255))
        screen.blit(text_start, (300,300))
        pygame.display.flip()

    #게임 진행
    SB = 0
    while SB == 0:
        screen.fill((255, 255, 255))
 
        #버튼 클릭 발생시
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #버튼이 클릭되었을 때, 점프 변수 활성화
            elif event.type == pygame.KEYDOWN:                
                if landing:
                    jump = True
                    landing = False
 
        #점프 변수 활성화 상태시, 공룡 좌표 이동(점프)
        if jump:
            dino_pos_y -= 10  #점프
        elif not jump and not landing:
            dino_pos_y += 10  #추락
 
        #공룡이 점프 상태인지 확인.
        if jump and dino_pos_y <= jump_max:
            jump = False

        #공룡이 점프 중일 때.
        if not landing and dino_pos_y >= Dino_bottom:
            landing = True
            dino_pos_y = Dino_bottom
        
        # 5초마다 나무 좌표 이동 속도 증가
        if second % 5 < 0.1:            
            tree_speed += 0.5
        second = pygame.time.get_ticks() / 1000

        #나무 좌표 이동
        tree_x -= tree_speed
        if tree_x <= -12:
            tree_x = MAX_WIDTH
            Score += 1

        #점수 표시
        font = pygame.font.Font("C:/Windows/Fonts/12롯데마트드림Bold.ttf", 20)
        text = font.render("Score : {}".format(Score), True, (80,80,80))
        screen.blit(text, (700,20))

        #나무 표시
        screen.blit(Tree, (tree_x, tree_y))
 
        #공룡 표시
        screen.blit(Dino, (dino_pos_x, dino_pos_y))

        #충돌 발생시, 반복문 탈출
        if (tree_x - (dino_pos_x+66)) <= 10 and (tree_y - (dino_pos_y + 16) <=13):
            Score = "Score : %d\n" % Score
            file.write(Score)
            GO = 1
            SB = 1

        #화면 갱신을 해주어야 화면에 적용이 되어짐.
        pygame.display.update()
        
        fps.tick(40)

    # 게임 종료 화면 
    while GO == 1:
        fps.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:                   
                    return GO == 0
                return main()
        screen.fill((0, 0, 0))
        font = pygame.font.Font("C:/Windows/Fonts/12롯데마트드림Bold.ttf", 40)
        text_over = font.render("GAME OVER", True, (255,255,255))
        screen.blit(text_over, (300,200))
        font = pygame.font.Font("C:/Windows/Fonts/12롯데마트드림Bold.ttf", 15)
        text_end = font.render("재시작을 원하시면 아무키나, 종료를 원하시면 X 버튼을 눌러주세요.", True, (255,255,255))
        screen.blit(text_end, (200,250))
        pygame.display.flip()

        
 
if __name__ == '__main__':
    main()
 