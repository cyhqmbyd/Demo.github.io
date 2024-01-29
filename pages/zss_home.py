'''主页'''
import streamlit as st
from PIL import Image
page=st.sidebar.radio(
    '主页',
    [
        '兴趣推荐',
        '图像处理',
        '智慧词典',
        '留言',
    ]
)

def page1():
    '''兴趣推荐'''
    st.write("你好")
    st.image("zhangshishuo_slogan.png")
    with open("zhangshishuo_霞光.mp3",'rb')as f:
        myMp3=f.read()
    st.audio(myMp3,format='audio/mp3',start_time=10)
    st.write('我的电影推荐')
    st.write('黄金三镖客')
    st.write('我的游戏推荐')
    st.write('原神')
    st.write('我的软件推荐')
    st.write('百度')

    
def page2():
    '''我的图像推荐'''
    st.write(':sunglasses:图像处理:sunglasses:')
    uploader_file=st.file_uploader('上传图片',type=['png','jpg','jpeg'])
    if uploader_file:
        file_name=uploader_file.name
        file_type=uploader_file.type
        file_size=uploader_file.size
        img= Image.open(uploader_file)
        st.image(img)
        tab1,tab2,tab3,tab4,tab5=st.tabs(['原图','改色1','改色2','改色3','改色4'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(2,1,0))
        with tab3:
            st.image(img_change(2,0,0))
        with tab4:
            st.image(img_change(1,0,2))
        
        st.image(img_change(img,0,1,2))

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
    '''智慧词典'''
    st.write(':sunglasses:life:sunglasses:')
    with open('zhangshishuo_words_space.txt','r',encoding='utf-8')as f:
        words_list=f.read().split('\n')
        #分割
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split('#')

    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]
    #统计次数
    with open('zhangshishuo_check_out_times.txt','r',encoding='utf-8')as f:
        times_list=f.read().split('\n')
            
    for i in range(len(times_list)):
        times_list[i]=times_list[i].split('#')
            
    time_dict={}
    for i in times_list:
        time_dict[int(i[0])]=int(i[1])
        
    #测试结果
    word=st.text_input('请输入查询单词')
    if word in words_dict:
        st.write(words_dict[word])
        #以n为zyn的代码
        n=words_dict[word][0]
        if n in time_dict:
            time_dict[n]+=1
        else:
            time_dict[n]=1
        st.write('查询次数:',time_dict[n])
        
        if word=='zhangshishuo':
            st.code('''#查无此料''')
            
    #time_dict
    with open('zhangshishuo_check_out_times.txt','w',encoding='utf-8')as f:
        message=''
        for k,v in time_dict.items():
            message +=str(k)+'#'+str(v)+'\n'
        message=message[:-1]
        f.write(message)
           


def page4():
    '''留言'''
    st.write(':sunglasses:评论:sunglasses:')
    with open('zhangshishuo_leave_messages.txt','r',encoding='utf-8')as f:
        messages_list=f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i]=messages_list[i].split('#')

    for i in messages_list:
        if i[1]=='阿短':
            with st.chat_message('☀'):
                st.write(i[1],':',i[2])
        elif i[1]=='编程猫':
            with st.chat_message('🍣'):
                st.write(i[1],':',i[2])
    name=st.selectbox('我是...',['阿短','编程猫'])
    new_message=st.text_input('想要说的话...')

    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open('zhangshishuo_leave_messages.txt','w',encoding='utf-8')as f:
            message=''
            for i in messages_list:
                message +=i[0]+'#'+i[1]+'#'+i[2]+'\n'
            message=message[:-1]
        f.write(message)

def img_change(img,rc,rb,rg):
    width,heigth=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(heigth):
            #rgb获取
            r=img_array[x,y][rc]
            g=img_array[x,y][rg]
            b=img_array[x,y][rb]
            img_array[x,y]=(b,g,r)
        return img

if page=='兴趣推荐':
    page1()
elif page=='图像处理':
    page2()
elif page=='智慧词典':
    page3()
elif page=='留言':
    page4()