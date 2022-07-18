import streamlit as st
import time
from PIL import Image

st.title('Streamlit おためし')

st.write('プログレスバーの表示')

'start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
   
    time.sleep(0.1)

'Done!!!'

image = Image.open('IMG_6314.PNG')
st.image(image, caption='成功！！！')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問合せ内容を書く')
expander2 = st.expander('問い合わせ2')
expander2.write('問合せ内容を書く')
expander3 = st.expander('問い合わせ3')
expander3.write('問合せ内容を書く')

#text = st.text_input('あなたの趣味を教えてください')
#condition = st.slider('あなたの今の調子は？',0, 100, 70)
#'あなたの趣味：',text
#'コンディション：',condition

#option = st.selectbox(
#   'あなたが好きな数字を教えてください',
#   list(range(1,11))
#    )

#'あなたの好きな数字は、', option, 'です。'


#if st.checkbox('Show Image'):
#    img = Image.open('IMG_5102.JPG')
#    img_rotate = img.rotate(-90)
#    st.image(img_rotate, caption='staba', use_column_width=True)

#df = pd.DataFrame(
#    np.random.rand(100,2)/[50, 50] + [35.507395, 139.440881],
#    columns=['lat','lon']
#)

#st.dataframe(df.style.highlight_max(axis=0))
#st.map(df)
