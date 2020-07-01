from hoshino import Service, Privilege as Priv

sv = Service('_help_', manage_priv=Priv.SUPERUSER, visible=False)

MANUAL = '''
=====================
- 巧克力使用说明 -
=====================
- 公主连接Re:Dive -
==================
公会战手册页面 https://w.url.cn/s/AX8j81U
公会战指令页面 https://w.url.cn/s/AxcGOeK
[会战查询] 查询国服会战数据，30分钟更新一次，接口由@Kengxxiao提供
[@bot来发十连] 十连转蛋模拟
[@bot来发单抽] 单抽转蛋模拟
[@bot来一井] 4w5钻！买定离手！
[查看卡池] 查看bot现在的卡池及出率
[.布丁ub3] 查询角色ub语音，格式为[.角色ub(1~6)] 括号里的数字代表ub语音序号，不用填括号，不填数字默认随机。
[.ubr] 随机查询一个角色的ub语音，别漏了点哦~
[竞技场查询 布丁 空花 黑骑 望 咕噜灵波]竞技场查询，接口由pcrdfans.com提供
[@bot妈] 给主さま盖章章
[pcr速查] 常用网址/速查表
[bcr速查] B服萌新攻略
[rank表] 查看rank推荐表
[十图装备] 查看B服十图的装备刷取指导
[黄骑充电表] 查询黄骑1动充电规律
[@bot官漫132] 官方四格阅览
[谁是春黑] 别称查询角色
[挖矿 15001] 查询矿场中还剩多少钻
[工资 1919] 查询今日竞技场结算钻石数
[切噜一下] 后以空格隔开接想要转换为切噜语的话
[切噜～♪切啰巴切拉切蹦切蹦] 切噜语翻译
===========
- 通用功能 -
===========
[.r] 掷骰子
[.r 3d12] 掷3次12面骰子
[@bot精致睡眠] 8小时精致睡眠(bot需具有群管理权限)
[给我来一份精致昏睡下午茶套餐] 叫一杯先辈特调红茶(bot需具有群管理权限)
[@bot来杯咖啡] 联系维护组，空格后接反馈内容
[#查询授权] 查询Bot在本群的到期时间
==========
- 群管理限定功能 -
=================
[翻译 もう一度、キミとつながる物語] 机器翻译
[lssv] 查看功能模块的开关状态
[禁用 pcr-arena-reminder-tw] 禁用背刺时间提醒(UTC+8)（群管理及以上可用）
[禁用 exp-reminder] 禁用经验药水购买提醒（群管理及以上可用）
[禁用 hourcall] 禁用时报（群管理及以上可用）
[大家问xxx你答yyy] 管理员调教bot答复，群内通用
[不要回答xxx] 删除调教的问题，xxx是问题而不是回答内容
=====================================
※※Powered By HoshinoBot※※
'''.strip()

@sv.on_command('help', aliases=('manual', '帮助', '说明', '使用说明', '幫助', '說明', '使用說明', '菜单', '菜單'), only_to_me=False)
async def send_help(session):
    await session.send(MANUAL)