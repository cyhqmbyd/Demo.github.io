'我的网络根据地'

import streamlit as st
from PIL import Image

page = st.sidebar.radio('我的首页\nMy homepage',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区'])

def page1():
    '我的兴趣推荐'
    st.title("    我的兴趣页      ")
    st.write("你好!")
    st.image("jym_cloudsea.jpg")
    st.write("")
    st.write("这里是我的主页")
    with open("jym_砕月~broken moon.mp3","rb") as f:
        myMp3 = f.read()
        st.audio(myMp3,format='audio/mp3',start_time = 0)
    st.write("")
    st.write("这里有数不尽的新颖玩意！")
    st.image("jym_on-ground.jpg")
    with open("jym_东风~eastern-wind.mp3","rb") as f:
        myMp3 = f.read()
        st.audio(myMp3,format='audio/mp3',start_time = 0)
    st.write("")
    st.write("希望大家在这儿都能快快乐乐~")
    st.image("jym_rocking-sky.png")
    with open("jym_绯想天~heart-red_sky.mp3","rb") as f:
        myMp3 = f.read()
        st.audio(myMp3,format='audio/mp3',start_time = 0)
    st.write("")
    st.write("无论何时何地，网络永远能是一隅避风港！")
    st.image("jym_broken-shelter.jpg")
    with open("jym_shelter.mp3","rb") as f:
        myMp3 = f.read()
        st.audio(myMp3,format='audio/mp3',start_time = 0)
    st.write("")
    
    st.link_button('东方project', 'https://thwiki.cc/%E9%A6%96%E9%A1%B5')
    st.link_button('chatgpt', 'https://52.gptchinese.app/chat/new')
    #https://52.gptchinese.app/chat/new

def img_change(img,rc,rg,rb):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            #获取rgb
            r = img_array[x,y][rc]
            g = img_array[x,y][rc]
            b = img_array[x,y][rb]
            img_array[x,y] = (b,g,r)
    return img

def page2():
    '''我的图片处理工具'''
    st.title(":rainbow:图像处理:rainbow:")
    uploader_file= st.file_uploader("上传图片",type=["png","jpg","jpeg"])
    if uploader_file:
        file_name = uploader_file.name
        file_type = uploader_file.type
        file_size = uploader_file.size
        img = Image.open(uploader_file)
        #st.image(img)
        tab1,tab2,tab3,tab4 = st.tabs(['原图','改色1','改色2','改色3'])
        with tab1:
            st.image(img)
    
        with tab2:
            st.image(img_change(img,1,2,1))
    
        with tab3:
            st.image(img_change(img,2,0,1))
    
        with tab4:
            st.image(img_change(img,1,1,1))
    
        st.image(img_change(img,0,1,2))

    

def page3():
    '''我的智慧词典'''
    st.title("我的智慧词典")
    with open('jym_words_space.txt', 'r', encoding='utf-8') as f:
        word_list = f.read().split('\n')
    #按照#号分割数据
    for i in range(len(word_list)):
        word_list[i] = word_list[i].split('#')
    # 转换成字典
    words_dict = {}
    for i in word_list:
        words_dict[i[1]] = [int(i[0]),i[2]]
        
    #统计单词查询次数
    with open('jym_check_out_times.txt','r',encoding='utf-8')as f:
        times_list = f.read().split('\n')
    #将数据读取出来后，获取单个的数据
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    time_dict = {}
    for i in times_list:
        time_dict[int(i[0])] = int(i[1])
        
    #测试结果
    word = st.text_input('请输入要查询的单词：')
    #显示结果
    if word in words_dict:
        st.write(words_dict[word])
        #n表示的编号
        n = words_dict[word][0]
        if n in time_dict:
            time_dict[n] += 1
        else:
            time_dict[n] = 1
        st.write('查询次数：',time_dict[n])
        if word == 'ShangHaiAlice':
            st.code('''
                    恭喜你触发彩蛋!
                    ''')
            with open("jym_童祭.mp3","rb") as f:
                        myMp3 = f.read()
                        st.audio(myMp3,format='audio/mp3',start_time = 0)
    st.balloons()
    st.snow()
    with open("jym_check_out_times.txt",'w',encoding='utf-8') as f:
        message = ''
        for k,v in time_dict.items():
            message += str(k)+'#'+str(v)+'\n'
        message = message[:1]
        f.write(message)
        
    
def page4():
    '''留言区'''
    st.title('留言区')
    with open('jym_leave_messages.txt','r',encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('😊'):
                st.write(i[1],":",i[2])
        elif i[1] == '编程猫':
            with st.chat_message('😁'):
                st.write(i[1],":",i[2])
    name = st.selectbox('我是……',['阿短','编程猫'])
    new_message = st.text_input('请输入你想要说的话:')
    
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open('jym_leave_messages.txt','w',encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)



    
if (page == '我的兴趣推荐'):
    page1()
elif (page == '我的图片处理工具') :
    page2()
elif (page == '我的智慧词典') :
    page3()
elif (page == '我的留言区') :
    page4()


