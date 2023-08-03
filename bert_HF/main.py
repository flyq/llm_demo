import torch
from transformers import BertModel, BertTokenizer, BertConfig, pipeline

tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
config = BertConfig.from_pretrained('bert-base-chinese')
config.update({'output_hidden_states':True}) # 这里直接更改模型配置
model = BertModel.from_pretrained("bert-base-chinese",config=config)

print(tokenizer.encode("生活的真谛是美和爱"))  # 对于单个句子编码
print(tokenizer.encode_plus("生活的真谛是美和爱","说的太好了")) # 对于一组句子编码

sentences = ['网络安全开发分为三个层级',
             '车辆系统层级网络安全开发',
             '车辆功能层级网络安全开发',
             '车辆零部件层级网络安全开发',
             '测试团队根据车辆网络安全目标制定测试技术要求及测试计划',
             '测试团队在网络安全团队的支持下，完成确认测试并编制测试报告',
             '在车辆确认结果的基础上，基于合理的理由，确认在设计和开发阶段识别出的所有风险均已被接受',]
test1 = tokenizer(sentences)

print(test1)  # 对列表encoder
print(tokenizer("网络安全开发分为三个层级"))  # 对单个句子encoder