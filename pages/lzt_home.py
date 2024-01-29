import streamlit as st
from PIL import Image 
import time

page = st.sidebar.radio(
    '我的主页',
    [
        '我的兴趣推荐',
        '我的图像处理工具',
        '我的智慧词典',
        '我的留言区',  
        '中国地理集', 
    ]
)

def page1():
    '''我的兴趣推荐'''
    st.header('你好,欢迎来到我的主页:smile:', divider='rainbow')
    st.balloons()
    st.subheader("我的电影推荐:clapper:")
    st.write("《千与千寻》是由宫崎骏执导的动画电影,主要讲述了:red[千寻意外来到神灵世界后,为了救因惩罚而变成猪的家人,经历许多磨难]的故事")
    col1, col2 = st.columns([1.11,1])
    with col1:
       st.image("千与千寻.jpg")
    with col2:
       st.image("千与千寻2.jpg")
    st.write("除了这个，宫崎骏的其他电影也非常值得我们一看，例如:blue[龙猫]、:blue[天空之城]等等:eyes:")
    st.image("龙猫.jpg")
    st.subheader(":arrow_up:龙猫")
    st.image("天空之城.jpg")
    st.subheader(":arrow_up:天空之城")
    st.write("----------------------")
    st.subheader(":headphones:我的音乐推荐:周杰伦《稻香》:musical_note::guitar:")
    with open("lzt_稻香.mp3","rb") as f:
        myMp3 = f.read()
    st.audio(myMp3,format='audio/mp3',start_time=53)
    st.write("-----------------------")
    st.subheader("我的美食推荐：披萨:spaghetti:和广东早茶:tea:")
    st.image("披萨.webp")
    st.write(":arrow_up:披萨是一种由特殊的酱汁和馅料做成的具有意大利风味的食品，但其实这种食品已经超越语言与文化的障碍，成为全球通行的小吃，受到各国消费者的喜爱。")
    st.image("广东早茶.webp")
    st.write(":arrow_up:广东人饮早茶，不仅仅是喝茶，已经演变成以吃茶点为主，茶点讲究精、美、新、巧。饮早茶已成为广东人生活中必不可少的一部分。在茶楼里，大家一边品尝美味，一边和家人朋友说东家长西家短。茶客们的声音此起彼伏，人与人之间的关系也逐渐拉近。在广东，“请早茶”成为一种普遍的社交方式。:orange[“饮咗茶未啊！”]成为广东人见面时最常说的一句话。")
    st.write(":red[特色茶点———虾饺、干蒸、叉烧包、奶黄包、流沙包、千层糕、肠粉、煎饺、马蹄糕......:face_with_hand_over_mouth:好吃极了！]")
    
    

def page2():
    '''我的图像处理工具'''
    st.write(':sunglasses:图片处理小程序:sunglasses:')
    uploader_file = st.file_uploader('上传图片',type=['png','jpg','jpeg'])
    if uploader_file:
        # 获取图片文件的名称、类型和大小 
        file_name = uploader_file.name
        file_type = uploader_file.type
        file_size = uploader_file.size
        img = Image.open(uploader_file)
        #st.image(img)
        tab1,tab2,tab3,tab4 = st.tabs(['原图','改色1','改色2','改色3'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,2,1,0))
        with tab3:
            st.image(img_change(img,1,0,2))
        with tab4:
            st.image(img_change(img,2,1,0))

def page3():
    '''我的智慧词典'''
    roading = st.progress(0, '开始加载')
    for i in range(1, 101, 1):
        time.sleep(0.02)
        roading.progress(i, '正在加载'+str(i)+'%')
    roading.progress(100, '加载完毕！')
    
    st.write("我的智慧词典")
    with open("lzt_words_space.txt",'r',encoding='utf-8') as f:
        word_list =f.read().split('\n')
    # 按照#号分割数据
    for i in range(len(word_list)):
        word_list[i] = word_list[i].split('#')
    # 转换成字典
    words_dict = {}
    for i in word_list:
        words_dict[i[1]] = [int(i[0]),i[2]]

    # 统计单词查询次数
    with open("lzt_check_out_times.txt",'r',encoding='utf-8') as f:
        times_list =f.read().split('\n')
    #数据读取后获取单个数据
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    
    # 创建输入框
    word = st.text_input('请输入要查询的的单词:')
    # 显示查询的内容
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1            
        st.write('查询次数：',times_dict[n])

        
        if word == "book":
            st.code('''
                    # 恭喜你触发彩蛋，这是一行python代码
                    print("hello world")
                    ''')
            st.balloons()
        elif word == "snow":
            st.code('''
                    恭喜你又触发彩蛋，这次是雪花飘落哦！
                    ''')
            st.snow()
            
    with open('lzt_check_out_times.txt','w',encoding='utf-8')as f:
        message = ''
        for k,v in times_dict.items():
            message += str(k) + '#'+ str(v)+ '\n'
        message =message[:-1]
        f.write(message)
    
    
def page4():
    '''我的留言区'''
    st.subheader(':speech_balloon:我的留言区:speech_balloon:', divider='blue')
    
    # 从文件中加载内容，并处理成列表
    with open("lzt_leave_messages.txt",'r',encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    #数据读取后获取单个数据
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🙂'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🐱'):
                st.write(i[1],':',i[2])
    st.subheader('', divider='blue')
    name = st.selectbox('我是......',['阿短','编程猫'])
    new_message = st.text_input("想要说的话......")
    
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open('lzt_leave_messages.txt','w',encoding='utf-8')as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1]+ '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

def page5():
    '''中国地理集'''
    st.subheader(":star::sparkles: Hi！这里是中国各地的著名景点:point_down:",divider='rainbow')
    st.snow()
    st.subheader(":one:西藏——布达拉宫、珠穆朗玛峰:snow_capped_mountain:")
    col3, col4 = st.columns([2,1.2])
    with col3:
       st.image("布达拉宫.jpg")
    with col4:
       st.image("珠穆朗玛峰.webp")
    st.write("布达拉宫位于中国西藏自治区首府拉萨市区西北的玛布日山上，是一座宫堡式建筑群，一说为吐蕃王朝赞普松赞干布为迎娶尺尊公主和文成公主而兴建。布达拉宫的壁画、木雕及建筑过程中使用的金属冶炼技术均闻名于世，体现了以藏族为主，汉、蒙、满各族能工巧匠高超的技艺。1961年，布达拉宫成为了中华人民共和国国务院第一批全国重点文物保护单位之一。1994年，布达拉宫被列为世界文化遗产。")
    st.write("珠穆朗玛峰，岩面高程8844.43米，雪面高程8848.86米，是喜马拉雅山脉中的主峰，位于中华人民共和国与尼泊尔边界上，位于东经86.9°，北纬27.9°，是一条近似东西向的弧形山系，它的北坡在中国青藏高原境内，南坡在尼泊尔境内。")
    st.subheader('', divider='red')
    
    st.subheader(":two:内蒙古——呼伦贝尔草原:sheep:")
    col5, col6 = st.columns([2,2])
    with col5:
       st.image("呼伦贝尔大草原.webp")
    with col6:
       st.image("草原.jpg")
    st.write("呼伦贝尔草原位于内蒙古自治区东北部，地处大兴安岭以西的呼伦贝尔高原上，因呼伦湖、贝尔湖而得名。呼伦贝尔草原是世界著名的天然牧场，是世界四大草原之一，被称为世界上最好的草原。")
    st.subheader('', divider='orange')
    
    st.subheader(":three:黄土高原:sunny:")
    st.image("黄土高原.jpg")
    st.write("黄土高原之上孕育了黄土地独特的文化，产生了以“窑洞”为代表的民居和以信天游、安塞腰鼓为代表的民间文艺。距今约5500年前，黄土高原西部史前人类已经开始从事以粟为主的旱作农业。")
    st.subheader('', divider='blue')
    
    st.subheader(":four:江南水乡")
    st.image("江南水乡.jpg")
    st.write(":blue[“江南好，风景旧曾谙；日出江花红胜火，春来江水绿如蓝。能不忆江南？”]这首诗总把人们的思绪牵到风景如画的江南。这里河湖交错，水网纵横，小桥流水、古镇小城、田园村舍、如诗如画。江南所处的长江三角洲和太湖水网地区，气候温和，季节分明，雨量充沛，因此形成了以水运为主的交通体系。居民的生产生活依赖着水，这种自然的环境和功能的需要，塑造了极富韵味的江南水乡民居的风貌与特色。")
    st.subheader('', divider='violet')
    
    st.subheader(":five:湖北——神农架")
    st.image("神农架.jpg")
    st.write("神农架之得名，联系着一则有关神农尝百草的古老传说：:green[远古时候，神农皇帝为遍尝百草率众寻到了一座高山上，但见这儿山势陡峭，森林遍野，认定必有奇药密藏，不禁喜出望外。他先教民“架木为屋，以避凶险”；继教民“架木为梯，以助攀缘”；采得了良药400种，著就了《神农本草经》。为向天帝复命，才“架木为坛，跨鹤飞天”而去。]后人缅怀始祖恩德，便将这座高山称做了神农架。")
    st.subheader('', divider='red')
    
    st.subheader(":six:杭州——西湖")
    st.image("西湖.jpg")
    st.write("西湖自古以来便流传着《白蛇传》《梁山伯与祝英台》《苏小小》等民间传说和神话故事。白蛇传中的“断桥相会”“白娘子被压雷峰塔”等情节与西湖十景有着联系。西湖还以其湖光山色和人文底蕴，吸引了历代文人墨客的眷顾，在文学方面留下了大量的诗词佳句，如：")
    st.write(":green[最爱湖东行不足，绿杨阴里白沙堤。———白居易《钱塘湖春行》]")
    st.write(":orange[欲把西湖比西子，淡妆浓抹总相宜。———苏轼《饮湖上初晴后雨（其二）》]")
    st.subheader('', divider='green')
    
    st.subheader(":seven:海南——西沙群岛:desert_island:")
    st.image("西沙群岛.jpg")
    st.write("西沙群岛，为中国南海诸岛四大群岛之一，是中国南海陆地面积最大的群岛，由海南省三沙市西沙区管辖。:blue[岛上热带植物茂盛，林木遍布，主要有麻疯桐、羊角树、椰子树:palm_tree:等，有“林岛”之称。]附近海域盛产热带鱼类、贝类、海龟等。蓝天碧海，椰树成行，风光旖旎，是典型的热带风光。")
    st.subheader('', divider='blue')
    
    st.subheader(":eight:泰山")
    st.image("泰山.jpg")
    st.write("泰山被古人视为“直通帝座”的天堂，成为百姓崇拜，帝王告祭的神山，有“泰山安，四海皆安”的说法。泰山是中华民族的象征，是东方文化的缩影，是“天人合一”思想的寄托之地，是中华民族精神的家园。")
    st.subheader('', divider='rainbow')
    
    st.subheader(":nine:北京——天坛、紫禁城")
    col7, col8 = st.columns([2,2.2])
    with col7:
       st.image("天坛.webp")
    with col8:
       st.image("紫禁城.jpg")
    st.write("天坛建筑处处展示着中国传统文化特有的寓意、象征的艺术表现手法，其主要建筑圆丘坛、祈年殿、皇穹宇都采用圆形平面，而祈年殿、圆丘坛的砖砌外墙则为方形，天坛内外两重坛垣也是北圆南方，寓意“天圆地方”。其技术构造也因建筑外形的特点和“天”的含义而采用奇数、年数等与之相关的数字，主体建筑屋面覆以蓝色琉璃瓦以象征青天，使祭礼达到神圣而崇高的效果。此外，天坛建筑集:red[古代哲学、历史学、数学、力学、美学、生态学]于一炉，:red[有着较高的历史价值、科学价值和独特的艺术价值，更有着深刻的文化内涵，既是时间与空间在建筑上的体现，又是建筑技术与艺术完美结合的产物]。")
    st.write("故宫又称紫禁城。中国古代讲究“天人合一”的规划理念，用天上的星辰与都城规划相对应，以突出政权的合法性和皇权的至高性。天帝居住在紫微宫，而人间皇帝自诩为受命于天的“天子”，其居所应象征紫微宫以与天帝对应，《后汉书》载“天有紫微宫，是上帝之所居也。王者立宫，象而为之”。紫微、紫垣、紫宫等便成了帝王宫殿的代称。由于封建皇宫在古代属于禁地，常人不能进入，故称“紫禁”。")
    st.write("---------------------------")


def img_change(img,rc,rg,rb):
    width,height = img.size
    image_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB
            r = image_array[x,y][rc]
            g = image_array[x,y][rc]
            b = image_array[x,y][rb]
            image_array[x,y] = (b,g,r)
    return img
    
if page =='我的兴趣推荐':
    page1()
elif page =='我的图像处理工具':
    page2()
elif page =='我的智慧词典':
    page3()
elif page =='我的留言区':
    page4()
elif page =='中国地理集':
    page5()