import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
response = requests.get(url)
print("Status Code:",response.status_code)
response_dict = response.json()
print(response_dict.keys())

print("Total Repositories:",response_dict['total_count'])
res_items_dic = response_dict['items']
print("Total Items",len(res_items_dic))

res_item_dic = res_items_dic[0]
print("Keys:",len(res_item_dic))

names=[]
stars=[]
for res_item_dic in res_items_dic:
    names.append(res_item_dic['name'])
    stars.append(res_item_dic['stargazers_count'])

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title="Most starred repositories in github"
chart.x_labels=names
chart.add('',stars)
chart.render_to_file("python_repo.svg")