from langchain_core.pydantic_v1 import BaseModel,Field
from typing import List


# 定义大模型最终返回的数据结构，供 PydanticOutputParser 解析使用。
class Xiaohongshu(BaseModel):
    # titles 固定要求生成 5 个小红书标题。
    titles:List[str]=Field(description="小红书的5个标题",min_items=5,max_items=5)

    # content 用于保存小红书正文内容。
    content:str=Field(description="小红书的正文内容")
