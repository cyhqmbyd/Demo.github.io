import streamlit as st
from PIL import Image
page = st.sidebar.radio('我的主页',['我的兴趣推荐','我的图像推荐','我的智慧词典','我的留言区',])

def page1():
    '''我的推荐'''
    st.write("你好")
    st.write('我的电影推荐')
    st.write('----------------------------')
    st.write('我喜欢的图片')
    st.image("lcz_slogan.png")
    st.write('我喜欢的音乐')
    with open("lcz_霞光.mp3","rb") as f:
        myMp3 = f.read()
    st.audio(myMp3,format='audio/mp3',start_time = 0)
    
    st.write('----------------------------')
    st.write('我的习题集推荐')
    st.write('----------------------------')
    
def page2():
    '''我的图像推荐'''
    st.write(':100:图像处理:100:')
    uploader_file = st.file_uploader('上传图片',type = ['png','jpg','jpeg'])
    if uploader_file:
        file_name = uploader_file.name
        file_type = uploader_file.type
        file_size = uploader_file.size
        img = Image.open(uploader_file)
        st.image(img)
        tab1,tab2,tab3,tab4 = st.tabs(['原图','改色1','改色2','改色3'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,1,2))
        with tab3:
            st.image(img_change(img,1,0,2))
        with tab4:
            st.image(img_change(img,1,2,0))
    
def page3():
    '''我的智慧词典'''
    st.write('我的智慧词典')
    with open('words_space.txt','r',encoding='utf-8') as f:
        word_list = f.read().split('\n')
    for i in range(len(word_list)):
        word_list[i] = word_list[i].split('#')
    words_dict = {}
    for i in word_list:
        words_dict[i[1]] = [int(i[0]),i[2]]
    word = st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(words_dict[word])
        if word == 'book':
            st.code('恭喜你触发彩蛋')
        
def page4():
    '''我的留言区'''
    pass

def img_change(img,rc,rg,rb):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][rg]
            b = img_array[x,y][rb]
            img_array[x,y]=(b,g,r)
    return img

if page == '我的兴趣推荐':
    page1()
elif page == '我的图像推荐':
    page2()
elif page == '我的智慧词典':
    page3()
elif page == '我的留言区':
    page4()