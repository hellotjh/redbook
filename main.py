import streamlit as st
from utils import *

# 页面标题：这是一个基于 Streamlit 的小红书文案生成工具。


st.header("爆款小红书AI写作助手")

# 侧边栏用于收集 API Key，避免把密钥写死在代码里。
with st.sidebar:
    openai_api_key = st.text_input("请输入OpenAI API密钥",type="password")
    st.markdown("[获取OpenAI API密钥](https://xcode.best/console)")

theme=st.text_input("主题")
submit=st.button("开始写作")

# 点击生成后，先校验 API Key 是否填写。
if submit and not openai_api_key:
    st.info("请输入API密钥！")
    st.stop()
    openai.api_key = openai_api_key
# 再校验主题是否填写，防止向模型发送空主题。
elif submit and not theme:
    st.info("请输入主题！")
    st.stop()
# 输入校验通过后，调用 LangChain 生成小红书标题和正文。
if submit:
    with st.spinner("AI正在努力创作中，请稍等..."):
        result=generate_xiaohongshu(theme,openai_api_key)
        st.success("生成成功！")
        st.divider()
        # 将 5 个标题和正文分成左右两列展示。
        left_column,right_column=st.columns(2)
        with left_column:
            st.markdown("##### 小红书标题1")
            st.write(result.titles[0])
            st.markdown("##### 小红书标题2")
            st.write(result.titles[1])
            st.markdown("##### 小红书标题3")
            st.write(result.titles[2])
            st.markdown("##### 小红书标题4")
            st.write(result.titles[3])
            st.markdown("##### 小红书标题5")
            st.write(result.titles[4])
        with right_column:
            st.markdown("##### 小红书正文")
            st.write(result.content)
