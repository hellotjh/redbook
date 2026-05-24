from langchain_openai import ChatOpenAI
from prompt_template import system_template_text,user_template_text
from langchain_core.prompts import ChatPromptTemplate
import os
from langchain.memory import ConversationBufferMemory
from langchain_core.output_parsers import PydanticOutputParser
from xiaohongshu_model import Xiaohongshu

# 下面是早期聊天记忆功能的测试代码，目前小红书生成主流程没有使用。
# memory = ConversationBufferMemory(return_messages=True)
# print(get_chat_response("牛顿提出过哪些知名的定律？", memory, os.getenv("OPENAI_API_KEY")))
# print(get_chat_response("我上一个问题是什么？", memory, os.getenv("OPENAI_API_KEY")))
def generate_xiaohongshu(theme,open_api_key):
    """根据用户输入的主题，生成结构化的小红书标题和正文。"""

    # 组合系统提示词和用户提示词，后续会把主题和输出格式说明填入模板。
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template_text),
        ("user", user_template_text)
    ])

    # 初始化聊天模型；base_url 指向 OpenAI 兼容接口。
    model = ChatOpenAI(model="gpt-5.5",api_key=open_api_key,base_url="https://xcode.best/v1/")

    # 使用 Pydantic 模型约束大模型输出，要求返回 titles 和 content。
    output_parser = PydanticOutputParser(pydantic_object=Xiaohongshu)

    # LCEL 管道：提示词模板 -> 聊天模型 -> 结构化输出解析器。
    chain=prompt|model|output_parser

    # parser_instructions 注入 system_template_text，theme 注入 user_template_text。
    result=chain.invoke({"parser_instructions": output_parser.get_format_instructions(),
                         "theme":theme})
    return result
