import streamlit as st
from PIL import Image
import time
page = st.sidebar.radio(
    '我的主页',
    [
        '我的兴趣推荐',
        '我的图像处理工具',
        '我的智慧字典',
        '我的留言区'
    ]
)

def page1():
    '''我的兴趣推荐'''
    st.write(':smile:你好:smile:,我是SCY')
    tab1, tab2, tab3 = st.tabs(['我的图片推荐', '我的音乐推荐', '我的游戏推荐'])
    with tab1:
        st.image('SCY_天象奇景.jpg')
    with tab2:
        with open('SCY_霞光.mp3', 'rb') as f:
            myMp3 = f.read()
        st.audio(myMp3, format = 'audio/mp3', start_time = 0)
    with tab3:
        st.write('我的世界')


def page2():
    '''我的图像来推荐'''
    st.write(':sunglasses:图片处理小程序:sunglasses:')
    uploaded_file = st.file_uploader('上传图片', type = ['png', 'jpg', 'jpeg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        fs = st.toggle('反色滤镜')
        bk = st.toggle('黑白滤镜')
        if fs and bk:
            progress(1)
            st.image((img_change(img_change(img, 0, 1, 2), 0, 0, 0)))
        elif fs:
            progress(2)
            st.image(img_change(img, 0, 1, 2))
        elif bk:
            progress(2)
            st.image(img_change(img, 0, 0, 0))
def progress(ge):
    roading = st.progress(0, '开始加载')
    time.sleep(5)
    for i in range(1, 101, ge):
        time.sleep(0.1)
        roading.progress(i, '正在加载'+str(i)+'%')      
    roading.progress(100, '加载完毕！')


        # tab1, tab2, tab3, tab4, tab5 = st.tabs(['原图', '改色1', '改色2', '改色3', '黑白'])
        # with tab1:
        #     st.image(img)
        # with tab2:
        #     st.image(img_change(img, 0, 2, 1))
        # with tab3:
        #     st.image(img_change(img, 1, 2, 0))
        # with tab4:
        #     st.image(img_change(img, 0, 1, 2))
        # with tab5:
        #     st.image(img_change(img, 0, 0, 0))
    #st.image(img_change(img, 0, 1, 2))

def img_change(img, rc, rg, rb):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            #获取RGB
            r = img_array[x, y][rc]
            g = img_array[x, y][rg]
            b = img_array[x, y][rb]
            img_array[x, y] = (b, g, r)
    return img         
def page3():
    '''我的智慧字典'''
    st.write('我的智慧字典')
    with open('SCY_words_space.txt', 'r', encoding='utf-8') as f:
        word_list = f.read().split('\n')
    #按照#分割数据
    for i in range(len(word_list)):
        word_list[i] = word_list[i].split('#')
    #转换成字典
    words_dict = {}
    for i in word_list:
        words_dict[i[1]] = [int(i[0]), i[2]] 
        
    with open('SCY_check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range (len(times_list)):
        times_list[i] = times_list[i].split('#')
    time_dict = {}
    for i in times_list:
        time_dict[int(i[0])] = int(i[1])
    #测试结果
    word = st.text_input('请输入要查询的单词:')
    #显示结果
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in time_dict:
            time_dict[n] += 1
        else:
            time_dict[n] = 1
        st.write('查询次数:', time_dict[n])
        if word == 'book':
            st.code('''
                    #恭喜你触发彩蛋,这是一行python代码
                    print('hello word')..
                    ''')
        elif word == 'balloon':
            st.balloons()
        elif word == 'snow':
            st.snow()
        elif word == 'shabby':
            st.code('我是个shabby')
        with open('SCY_check_out_times.txt', 'w', encoding='utf-8') as f:
            message =  ''
            for k, v in time_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
def page4():
    '''我的留言区'''
    st.write('我的留言区')
    with open('SCY_leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '我':
            with st.chat_message('💙'):
                st.write(i[1], ':', i[2])
        elif i[1] == 'SCY':
            with st.chat_message('💢'):
                st.write(i[1], ':', i[2])
        elif i[1] == '作者':
            with st.chat_message('?'):
                st.write(i[1], ':', i[2])
    name = st.selectbox('我是......', ['我', 'SCY', '作者'])
    new_message = st.text_input('想要说的话......')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
    with open('SCY_leave_messages.txt', 'w', encoding='utf-8') as f:
        message = ''
        for i in messages_list:
            message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
        message = message[:-1]
        f.write(message)
        
if page == '我的兴趣推荐':
    page1()
elif page == '我的图像处理工具':
    page2()
elif page == '我的智慧字典':
    page3()
elif page == '我的留言区':
    page4()
    