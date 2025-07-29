import streamlit as st
import streamlit.components.v1 as htmlviewer
st.set_page_config(layout='wide', page_title='음운 변동의 규칙 알기!!!')

# Title Msg#1
st.title('음운의 변동 양상을 종류별로 분류해봅시다.')
with open('./index.html', 'r', encoding='utf-8') as f:
    html = f.read()
    f.close()

# html = '''
# <html>
#    <head>
#        <title> this is my html </title>
#    </head>
#    <body>
#        <h1>Topic</h1>
#        <h2>SubTopic</h2>
#   </body>
# </html>
# '''

# Box#1(4), Box#2(1)
col1, col2 = st.columns((4,1))
with col1:
    with st.expander('참고 동영상'):
        url = 'https://www.youtube.com/watch?v=XyEOEBsa8I4'
        st.info('Content..')
        st.video(url)
    with st.expander('음운의 변동 종류 4가지'):
        st.info('교체, 탈락, 첨가, 축약')
        imgfilepath = 'language.jpg'
        st.image(imgfilepath)
    with st.expander('음운의 변동 문제'):
        st.write(html, unsafe_allow_html=True)
        htmlviewer.html(html)
    with st.expander('정리해봅시다'):
        imgfilepath = 'flowchart.jpg'
        st.image(imgfilepath)

with col2:
    with st.expander('Tips..'):
        st.info('Tips..')
    with st.expander('예시'):
        st.info('국밥[국빱]은 교체, 좋아[조아]은 탈락, 좋다[조타]는 축약, 솜이불[솜니불]은 첨가')
    with st.expander('Tips..'):
        st.info('Tips..')
    with st.expander('정답'):
        st.info('국수는 교체이므로 (가), 낳은은 첨가이므로 (나), 국화는 탈락이므로 (다), 담요는 축약이므로 (라))')
st.markdown('<hr>', unsafe_allow_html=True)
st.write('<font color="BLUE">(c)copyright. all rights reserved by Kim', unsafe_allow_html=True)