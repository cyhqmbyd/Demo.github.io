import streamlit as st
from PIL import Image

page = st.sidebar.radio("我的首页", ["我的兴趣推荐", "我的图像来推荐", "我的智慧词典", "我的留言区"])

def page1():
    '''我的推荐'''
    st.write("您好")
    st.write('我的电影推荐')
    st.write('-----------------------------')
    st.write('我喜欢的图片')
    # st.image("bcm_slogan.png")
    st.write('-----------------------------')
    st.write('我的音乐推荐')
    with open('lcz_歌曲.mp3','rb') as f:
        mymp3 = f.read()
    st.audio(mymp3,format = 'audio/mp3', start_time = 0)
    
    st.write('-----------------------------')
    st.write('我的习题集推荐')
    st.write('-----------------------------')

def page2():
    '''我的图像来推荐'''
    st.write(':100:图像处理:100:')
    uploader_file = st.file_uploader('上传图片',type = ['png','jpg','jpeg'])
    if uploader_file:
        file_name = uploader_file.name
        file_type = uploader_file.type
        file_size = uploader_file.size
        img = Image.open(uploader_file)
        # st.image(img)
        tab1,tab2,tab3,tab4 = st.tabs(['原图','改色1','改色2','改色3'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,2,1,0))
        with tab3:
            st.image(img_change(img,1,0,2))
        with tab4:
            st.image(img_change(img,0,1,0))

    col1,col2 = st.columns([2,1])
    with col1:
        st.image('6.png')
        col3,col4 = st.columns([1,1])
        with col3:
            st.image('1.png')
        with col4:
            st.image('2.png')
    with col2:
        st.image('5.png')
    
def page3():
    '''我的智慧词典'''
    st.write('我的智慧词典')
    with open('SCY_words_space.txt', 'r', encoding='utf-8') as f:
        word_list = f.read().split('\n')
    #按照#号分割数据
    for i in range(len(word_list)):
        word_list[i] = word_list[i].split('#')
    # 转换成字典
    words_dict = {}
    for i in word_list:
        words_dict[i[1]] = [int(i[0]),i[2]]
        
    #统计单词查询次数
    with open('lcz_check_out_times.txt','r',encoding='utf-8')as f:
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

        if word == 'book':
            st.code('''
                    # 恭喜你触发彩蛋，这是一行python代码
                    print('hello word')
                    ''')
    #time_dict   {1:13} keys()  values()
    with open('lcz_check_out_times.txt','w',encoding='utf-8')as f:
        message = ''
        for k,v in time_dict.items():
            message += str(k)+'#'+str(v)+'\n'
        message = message[:-1]
        f.write(message)
        
def page4():
    '''我的留言区'''
    st.write('我的留言区')
    #从文本中加载内容，并处理成列表
    with open('lcz_leave_messages.txt','r',encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')

    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('☀'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🍭'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是......', ['阿短','编程猫'])
    new_message = st.text_input('想要说的话......')
    
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open('lcz_leave_messages.txt','w',encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

def img_change(img,rc,rg,rb):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            #获取RGB[200,100,56]
            r = img_array[x,y][rc]
            g = img_array[x,y][rc]
            b = img_array[x,y][rb]
            img_array[x,y]=(b,g,r)
    return img

if page == "我的兴趣推荐":
    page1()
elif page == "我的图像来推荐":
    page2()
elif page == "我的智慧词典":
    page3()
elif page == "我的留言区":
    page4()
    