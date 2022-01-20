from mcdreforged.api.all import *
import time

def on_load(server: PluginServerInterface, info: Info):
	server.register_command(Literal('!!eztp').runs(check_player_list).then(Text("player").runs(lambda src, ctx:parse_tp_request(src,ctx['player']))))
	server.register_help_message('!!eztp','查询在线玩家列表，并通过点击传送至其他玩家')

def parse_tp_request(source: CommandSource, target_player):
	source.reply(f'teleported you to the {target_player}')
	source.get_server().execute(f'/tp {source.player} {target_player}')

@new_thread('EZTP_Main')
def check_player_list(source: CommandSource):
	api = source.get_server().get_plugin_instance('minecraft_data_api')
	player_number, player_number_limit, player_list = api.get_server_player_list()
	#server.reply(info, player_list)
	for i in range(player_number):
		display_text = RText(player_list[i],RColor.red)
		display_text = RTextBase.join(RText(''),['[',display_text,']'])
		display_text = display_text.set_hover_text(RText(f'click me to teleport to {player_list[i]}', RColor.yellow)).set_click_event(RAction.run_command,f'!!eztp {player_list[i]}')
		source.reply(display_text)
	


