import streamlit as st
# 1
# st.write('안녕! 친구야')

# 2
# st.text('이건 그냥 텍스트')
# my_text = '이건 변수에 저장한 텍스트'
# st.text(my_text)

# st.markdown("어떤 글씨는 **볼드**로, 어떤 글씨는 *이탤릭*으로 표시할께")
# st.markdown("""
# |이름|나이|직업|
# |-------|-----|----------|
# |홍길동|25|개발자|
# |김철수|30|데이터 분석가|
# |이영희|28|디자이너|                                    
# """)

# st.title('제목')
# st.header('1장')
# st.subheader('1절')
# st.text('안녕')

# st.write('이건 그냥 텍스트')
# my_text='이건 **변수**에 저장한 *텍스트*'
# st.write(my_text)

# st.write('# 제목')
# st.write('## 1장')
# st.write('### 1절')
# st.write('안녕')

# st.write(123)
# st.write(10+20)
# my_list=[1,2,3,4,5]
# st.write(my_list)
# my_dict={'이름':'홍길동','나이':25,'지역':'서울'}
# st.write(my_dict)

#3
# st.write('첫 번째 텍스트')
# st.write('두 번째 텍스트')
# st.write('세 번째 텍스트')

# col1, col2 = st.columns(2)
# with col1:
#     st.write('왼쪽 열~')
# with col2:
#     st.write('오른쪽 열!')

# col1, col2 = st.columns(2)
# with col1:
#     st.write('왼쪽 열~')
#     st.write('이제부터 왼쪽 열만 사용합니다.')

# col1, col2, col3 = st.columns([1,3,1])
# with col1:
#     st.write('첫 번째 열')
# with col2:
#     st.write('가운데 열 - 가장 넓은 열')
# with col3:
#     st.write('세 번째 열')

# with st.sidebar:
#     st.title('사이드바_제목')
#     st.write('사이드바에 표시할 텍스트')

# st.set_page_config(
#     initial_sidebar_state='collapsed'
# )
# with st.sidebar:
#     st.title('사이드바')
#     st.write('사이드바에 표시될 텍스트입니다.')

# st.set_page_config(
#     page_title='AI 프로그램',
#     page_icon='🤖',
#     layout='wide'
# )

# col1, col2 = st.columns(2)
# with col1:
#     st.write('첫 번째 열입니다.')
#     st.write('안녕하세요!')
# with col2:
#     st.write('두 번째 열입니다.')
#     st.write('반갑습니다!')

# button = st.button('클릭하세요.')
# if button:
#     st.write('버튼을 클릭한 경우에만 출력하는 내용')

# button = st.link_button('네이버로 가자.','https://naver.com')

# user_text = st.text_input('무슨 과일을 좋아하세요?')
# if user_text:
#     st.write(f'당신은 {user_text}를 좋아하는군요.')

# user_input=st.chat_input('무슨 과일을 좋아하세요?')
# if user_input:
#     st.write(f'당신은 {user_input}를 좋아하는군요.')

# option = st.selectbox('좋아하는 과일을 선택하세요.',['사과','바나나','체리'])
# st.write(f'선택한 과일: {option}')

# options = st.multiselect('좋아하는 과일을 모두 선택하세요.',['사과','바나나','체리'])
# st.write(f'선택한 과일들: {options}')

# uploaded_file = st.file_uploader('파일을 입력하세요: ')

# uploaded_file = st.file_uploader('파일을 업로드하세요. ')
# if uploaded_file:
#     st.write(uploaded_file.name, uploaded_file.size)
#     file_content = uploaded_file.read().decode('utf-8')
#     st.write(file_content)

# data = '''여러 줄의 예제 텍스트를 작성해 다운로드 기능을 테스트합니다.
# 이 텍스트는 Streamlit에서 다운로드 버튼을 누르면 저장합니다.
# 예제 텍스트를 다운로드해 기능을 확인해보세요.
# '''
# download_button = st.download_button(
#     '텍스트 다운로드',
#     data = data,
#     file_name='결과.txt'
# )

# counter = 0
# button = st.button('카운터 증가')
# if button:
#     counter+=1
# st.write(counter)

# if 'counter' not in st.session_state:
#     st.session_state.counter=0
# button= st.button('카운터 증가')
# if button:
#     st.session_state.counter+=1
# st.write(st.session_state.counter)

if 'counter1' not in st.session_state:
    st.session_state.counter1=0
if 'counter2' not in st.session_state:
    st.session_state.counter2=0
if 'counter3' not in st.session_state:
    st.session_state.counter3=0
button1 = st.button('카운터1: 1부터 시작해 1씩 증가')
button2 = st.button('카운터2: 2부터 시작해 2씩 증가')
button3 = st.button('카운터3: 3부터 시작해 3씩 증가')

if button1:
    st.session_state.counter1+=1
if button2:
    st.session_state.counter2+=2
if button3:
    st.session_state.counter3+=3
st.write(f'카운터1: {st.session_state.counter1}')
st.write(f'카운터2: {st.session_state.counter2}')
st.write(f'카운터3: {st.session_state.counter3}')