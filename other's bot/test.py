import sys
import re

text = """
<!DOCTYPE HTML>
<html>
<head>
	<title>chansey (370|513) - Tribal Wars - World 75</title>
	<meta http-equiv="content-type" content="text/html; charset=UTF-8" />
	<link id="favicon" rel="shortcut icon"  href="/favicon.ico" />

	<link rel="stylesheet" type="text/css" href="/merged/game.css?1403016825" />

		
	<script type="text/javascript" src="/merged/game.js?1403016825"></script>

			<script type="text/javascript" src="/js/game/QuestArrows.js?1401182916"></script>

	
	
	
	
	<script type="text/javascript">
        //<![CDATA[
        var sds = false;
		var image_base = "http://cdn.tribalwars.net/graphic/";
		var mobile = false;
		var mobile_on_normal = false;
		var premium = false;
		var server_utc_diff = 3600;

		var game_data = {"player":{"name":"egg whites","ally":"2147","sitter":"0","sleep_start":"0","sitter_type":"normal","sleep_end":"0","sleep_last":"0","interstitial":"0","email_valid":"1","villages":"1","incomings":"0","supports":0,"knight_location":null,"knight_unit":null,"rank":1006,"points":"1213","date_started":"1402411228","is_guest":"0","id":"10461385","quest_progress":"0","premium":false,"account_manager":false,"farm_manager":false,"points_formatted":"1<span class=\"grey\">.<\/span>213","rank_formatted":"1<span class=\"grey\">.<\/span>006","pp":"0","fire_pixel":"0","new_forum_post":"0","new_igm":"0","new_report":"0","new_quest":"1"},"village":{"id":18518,"name":"chansey","wood_prod":0.29854490389461,"stone_prod":0.25667635859605,"iron_prod":0.34724296436552,"storage_max":"18037","pop_max":"2216","wood_float":2192.3374727271,"stone_float":3592.6630757202,"iron_float":1653.0294931929,"wood":2192,"stone":3593,"iron":1653,"pop":"1886","x":"370","y":"513","trader_away":"1","bonus_id":null,"bonus":null,"buildings":{"village":"18518","main":"10","farm":"15","storage":"15","place":"1","barracks":"6","church":"0","church_f":"0","smith":"7","wood":"22","stone":"21","iron":"23","market":"1","stable":"3","wall":"10","garage":"0","hide":"2","snob":"0","statue":"0"},"player_id":"10461385","res":[2192,0.29854490389461,3593,0.25667635859605,1653,0.34724296436552,"18037","1886","2216"],"coord":"370|513"},"nav":{"parent":3},"link_base":"\/game.php?village=18518&amp;screen=","link_base_pure":"\/game.php?village=18518&screen=","csrf":"e049","world":"en75","market":"en","RTL":false,"version":"20825 8.24","majorVersion":"8.24","screen":"place","mode":"units","device":"desktop"};
		var csrf_token = 'e049';
			
		UI.AutoComplete.url = '/game.php?village=18518&ajaxaction=autocomplete&h=e049&screen=api';
		ScriptAPI.url = '/game.php?village=18518&ajax=save_script&screen=api';
		ScriptAPI.version = parseFloat(game_data.majorVersion);

		
		var userCSS = false;
		
		var isIE7 = false;

		var topmenuIsAlwaysVisible = false;
					topmenuIsAlwaysVisible = true;
		
		
				VillageContext._urls.overview = '/game.php?village=__village__&screen=overview';
		VillageContext._urls.info = '/game.php?village=18518&id=__village__&screen=info_village';
		VillageContext._urls.fav = '/game.php?village=18518&id=__village__&ajaxaction=add_target&h=e049&json=1&screen=info_village';
		VillageContext._urls.unfav = '/game.php?village=18518&id=__village__&ajaxaction=del_target&h=e049&json=1&screen=info_village';
		VillageContext._urls.claim = '/game.php?village=18518&id=__village__&ajaxaction=toggle_reserve_village&h=e049&json=1&screen=info_village';
		VillageContext._urls.market = '/game.php?village=18518&mode=send&target=__village__&screen=market';
		VillageContext._urls.place = '/game.php?village=18518&target=__village__&screen=place';
		VillageContext._urls.recruit = '/game.php?village=__village__&screen=train';
		VillageContext._urls.map = '/game.php?village=18518&id=__village__&screen=map';
		VillageContext._urls.unclaim = VillageContext._urls.claim;
				

		
		$(document).ready( function() {
			UI.ToolTip( $( '.group_tooltip' ), { delay: 1000 } );
			VillageContext.init();

		});

		
		//]]>
	</script>
	<!--[if IE 8]>
		<style type="text/css">
			/*
				Workaround for IE8 textarea scroll bug, see

				http://grantovich.net/posts/2009/06/that-weird-ie8-textarea-bug/

				You also need to set an absolute height for the element. since this depends
				on the location of the textarea, use an element style.
			*/
			textarea.ie8scrollfix { width: 300px !important; min-width: 98%; max-width: 98%;}
					</style>
	<![endif]-->
</head><body id="ds_body" class=" ">
	
	
	<div class="top_bar">
		<div class="bg_left"> </div>
		<div class="bg_right"> </div>
	</div>
	<div class="top_shadow"> </div>
	<div class="top_background"> </div>
    <div class="questlog_placeholder">&nbsp;</div>

	<table id="main_layout" cellspacing="0">
		<tr style="height: 48px;">
			<td class="topbar left fixed"></td>
			<td class="topbar center fixed">
				<div id="topContainer">
					<table id="topTable" style="text-align: center;" cellspacing="0">
						<tr>
							<td style="text-align: center;">
								<table class="menu nowrap" style="white-space: nowrap; ">
									<tr id="menu_row">
										<td class="menu-side"></td>
										<td class="menu-item"><a href="/game.php?village=18518&amp;screen=overview" >Overview</a></td>
										<td class="menu-item"><a href="/game.php?village=18518&amp;screen=map">Map</a></td>
										<td class="menu-item"><a href="/game.php?village=18518&amp;screen=report"><span id="new_report" class="icon header new_report" style="display: none" title="New report"></span> Reports</a><table cellspacing="0" class="menu_column"><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=all&amp;screen=report">All</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=attack&amp;screen=report">Attacks</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=defense&amp;screen=report">Defenses</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=support&amp;screen=report">Support</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=trade&amp;screen=report">Trade</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=other&amp;screen=report">Misc</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=forwarded&amp;screen=report">Forwarded</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=public&amp;screen=report">Public</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=filter&amp;screen=report">Filter</a></td></tr><tr><td class="bottom"><div class="corner"></div><div class="decoration"></div></td></tr></table></td>
										<td class="menu-item"><a href="/game.php?village=18518&amp;screen=mail"><span id="new_mail" class="icon header new_mail" style="display: none" title="New message"></span> Mail</a><table cellspacing="0" class="menu_column"><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=in&amp;screen=mail">Mail</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=mass_out&amp;screen=mail">Circular mail</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=new&amp;screen=mail">Write message</a></td></tr><tr><td class="bottom"><div class="corner"></div><div class="decoration"></div></td></tr></table></td>
																					<td>
																									<a class="manager_icon" style="background-image:url('http://dsen.innogamescdn.com/8.24/20825/graphic/icons/farm_assistent.png?e5a99')" href="/game.php?village=18518&amp;screen=am_farm" title="Farm Assistant">&nbsp;</a>
																																					<a class="manager_icon" style="background-image:url('http://dsen.innogamescdn.com/8.24/20825/graphic/icons/account_manager.png?ae0c3')" href="/game.php?village=18518&amp;screen=accountmanager" title="Account Manager">&nbsp;</a>
																							</td>
																				<td class="menu-item lpad"> </td>
																				<td class="menu-item" id="topdisplay">
											<div class="bg">
												<a href="/game.php?village=18518&amp;screen=ranking">Ranking</a>
												<div class="rank">(<span id="rank_rank">1<span class="grey">.</span>006</span>.|<span id="rank_points">1<span class="grey">.</span>213</span> P)</div>
												<table cellspacing="0" class="menu_column"><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=ally&amp;screen=ranking">Tribes</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=player&amp;screen=ranking">Players</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=secrets&amp;screen=ranking">Secrets</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=con_ally&amp;screen=ranking">Continent Tribes</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=con_player&amp;screen=ranking">Continent Players</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=kill_ally&amp;screen=ranking">Opponents defeated (tribe)</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=kill_player&amp;screen=ranking">Opponents defeated</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=awards&amp;screen=ranking">Achievements</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=wars&amp;screen=ranking">Wars</a></td></tr><tr><td class="bottom"><div class="corner"></div><div class="decoration"></div></td></tr></table>
											</div>
										</td>
																				<td class="menu-item rpad"> </td>
										<td class="menu-item"><a href="/game.php?village=18518&amp;screen=ally">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tribe</a><div class="buttonicon"><a href="/game.php?village=18518&amp;mode=forum&amp;screen=ally"  style="display:inline"><span id="tribe_forum_indicator" class="icon header no_new_post" title="No new posts in the tribe forum"></span></a></div><table cellspacing="0" class="menu_column"><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=overview&amp;screen=ally">Overview</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=properties&amp;screen=ally">Profile</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=members&amp;screen=ally">Members</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=contracts&amp;screen=ally">Diplomacy</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=tribalwars&amp;screen=ally">Wars</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=reservations&amp;screen=ally">Noble planner</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=forum&amp;screen=ally">Tribal forum</a></td></tr><tr><td class="bottom"><div class="corner"></div><div class="decoration"></div></td></tr></table></td>
										<td class="menu-item">
											<a href="/game.php?village=18518&amp;screen=info_player">
												Profile <span id="new_items" class="badge"></span>
											</a>
											<table cellspacing="0" class="menu_column"><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;screen=info_player">egg whites</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;screen=inventory">Inventory</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=awards&amp;screen=info_player">Achievements</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;screen=buddies">Friends</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=block&amp;screen=info_player">Block list</a></td></tr><tr><td class="bottom"><div class="corner"></div><div class="decoration"></div></td></tr></table>
										</td>
										<td class="menu-item">
											<a href="/game.php?village=18518&amp;screen=premium">
												<span class="coinbag coinbag-header"></span>&nbsp;<span id="premium_points">0</span>
												<span id="premium_points_buy"></span>
											</a>
											<table cellspacing="0" class="menu_column"><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=use&amp;screen=premium">Subscriptions</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=premium&amp;screen=premium">Purchase</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=transfer&amp;screen=premium">Transfer</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=log&amp;screen=premium">Points log</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=feature_log&amp;screen=premium">Feature log</a></td></tr><tr><td class="bottom"><div class="corner"></div><div class="decoration"></div></td></tr></table>
										</td>
										<td class="menu-item"><a href="/game.php?village=18518&amp;screen=settings">Settings</a><table cellspacing="0" class="menu_column"><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=settings&amp;screen=settings">Game options</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=account&amp;screen=settings">Account</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=move&amp;screen=settings">Start over</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=notify&amp;screen=settings">Notifications</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=share&amp;screen=settings">Connection sharing</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=vacation&amp;screen=settings">Account Sitting</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=logins&amp;screen=settings">Logins</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=poll&amp;screen=settings">Surveys</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=ref&amp;source=settings_menu&amp;screen=settings">Invite players</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;action=set_mobile&amp;h=e049&amp;mobile=1&amp;screen=settings">Mobile version</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=push&amp;screen=settings">Push notifications</a></td></tr><tr><td class="menu-column-item"><a href="/game.php?village=18518&amp;mode=ticket&amp;screen=settings" target="_blank">Support ticket</a></td></tr><tr><td class="bottom"><div class="corner"></div><div class="decoration"></div></td></tr></table></td>
										<td class="menu-side"><img src="http://dsen.innogamescdn.com/8.24/20825/graphic/loading.gif?4c84a" id="loading_content" style="display: none" alt="" class="" /></td>
									</tr>
								</table>
							</td>
						</tr>
					</table>
				</div>
			</td>
			<td class="topbar right fixed"> </td>

		</tr>
		<tr class="shadedBG">

			<td class="bg_left" id="SkyScraperAdCellLeft">
				<div id="SkyScraperAdLeft"></div>				<div class="bg_left"> </div>
			</td>

			<td class="maincell" style="width: 850px;">
							<div style="position:relative;">
					<div id="questlog" class="questlog">
																		<div 
								id="quest_34" 
								data-id="34"
								data-progress="0" 
								data-goals="7"
								data-url="/game.php?village=18518&amp;ajax=quest_show&amp;quest=34&amp;screen=api"
								class="quest opened  " 
								title="Conquer new land"
								style="background-image:url( 'http://dsen.innogamescdn.com/8.24/20825/graphic/buildings/snob.png?16792' );">
								<div class="quest_progress"></div>
								<img src="http://dsen.innogamescdn.com/8.24/20825/graphic/quests/check.png?29f73" border="0" style="position: absolute; left: 12px; top: 12px; display: none" alt="" class="" />
															</div>
													<div 
								id="quest_38" 
								data-id="38"
								data-progress="0" 
								data-goals="1"
								data-url="/game.php?village=18518&amp;ajax=quest_show&amp;quest=38&amp;screen=api"
								class="quest opened  " 
								title="Loyal Followers"
								style="background-image:url( 'http://dsen.innogamescdn.com/8.24/20825/graphic/icons/spear.png?48b3b' );">
								<div class="quest_progress"></div>
								<img src="http://dsen.innogamescdn.com/8.24/20825/graphic/quests/check.png?29f73" border="0" style="position: absolute; left: 12px; top: 12px; display: none" alt="" class="" />
															</div>
												<script>
						$(function() {
							Quests.init();
						});
						</script>					</div>
				</div>
			
			
			<br class="newStyleOnly" />
	        
			<hr class="oldStyleOnly" />

			<table id="header_info" align="center" width="100%" cellspacing="0">
				<colgroup>
					<col width="1%" />
					<col width="96%" />
					<col width="1%" />
					<col width="1%" />
					<col width="1%" />
				</colgroup>
				<tr>
					<td class="topAlign">
						<table class="header-border">
	                        <tr>
	                            <td>
									<table class="box menu nowrap">
	                                    <tr id="menu_row2">
																																																							<td style="white-space:nowrap;" id="menu_row2_village" class="firstcell box-item icon-box nowrap">
												<a class="nowrap" href="/game.php?village=18518&amp;screen=overview"><span class="icon header village"></span>chansey</a>
											</td>
																						<td class="box-item" style="padding-right: 6px"><b class="nowrap">(370|513) K53</b></td>
												                                    </tr>
	                                </table>
	                            </td>
	                        </tr>
							<tr class="newStyleOnly">
								<td class="shadow">
									<div class="leftshadow"> </div>
									<div class="rightshadow"> </div>
								</td>
							</tr>
	                    </table>
                	</td>

				<td align="right" class="topAlign"> </td><!-- flexible gap -->

				<td align="right" class="topAlign">
								</td>


                <td align="right" class="topAlign">
					<table align="right" class="header-border menu_block_right">
						<tr>
							<td>
								<table class="box smallPadding" cellspacing="0" style="empty-cells:show;">
									<tr style="height: 20px;">
										<td class="box-item icon-box firstcell">
											<a href="/game.php?village=18518&amp;screen=wood" title="Wood - 1075 per hour"><span class="icon header wood"> </span></a>
										</td>
                                        <td class="box-item" style="position: relative">
                                        	<span id="wood" title="Wood - 1075 per hour" class="res">2192</span>
                                        </td>
                                        <td class="box-item icon-box">
                                        	<a href="/game.php?village=18518&amp;screen=stone" title="Clay - 924 per hour"><span class="icon header stone"> </span></a>
                                        </td>
                                        <td class="box-item">
                                        	<span id="stone" title="Clay - 924 per hour" class="res">3593</span>
                                        </td>
                                        <td class="box-item icon-box">
                                        	<a href="/game.php?village=18518&amp;screen=iron" title="Iron - 1250 per hour"><span class="icon header iron" > </span></a>
                                        </td>
										<td class="box-item">
											<span id="iron" title="Iron - 1250 per hour" class="res">1653</span>
										</td>
                                        <td class="box-item icon-box">
                                        	<a href="/game.php?village=18518&amp;screen=storage" title="Storage capacity"><span class="icon header ressources"> </span></a>
                                        </td>
                                        <td class="box-item">
                                        	<span id="storage" title="Storage capacity">18037</span>
                                        </td>
									</tr>
								</table>
							</td>
						</tr>
						<tr class="newStyleOnly">
							<td class="shadow">
								<div class="leftshadow"> </div>
								<div class="rightshadow"> </div>
							</td>
						</tr>
					</table>
				</td>
				<td align="right" class="topAlign">
					<table class="header-border menu_block_right">
						<tr>
							<td>
								<table class="box smallPadding" cellspacing="0">
									<tr>
										<td class="box-item icon-box firstcell"><a href="/game.php?village=18518&amp;screen=farm" title="Farm"><span class="icon header population"> </span></a></td>
                                        <td class="box-item" align="center" style="margin:0;padding:0;" title="Farm">
                                        	<span id="pop_current_label">1886</span>/<span id="pop_max_label">2216</span>
                                        	<span style="display:none">
                                        		<span id="pop_current">1886</span>/<span id="pop_max">2216</span>
                                        	</span>
                                        </td>
                                    </tr>
								</table>
							</td>
						</tr>
						<tr class="newStyleOnly">
							<td class="shadow">
								<div class="leftshadow"> </div>
								<div class="rightshadow"> </div>
							</td>
						</tr>
					</table>
				</td>

				
				<td class="topAlign  " id="header_commands">
					<table class="header-border menu_block_right">
						<tr>
							<td>
								<table class="box smallPadding no-gap" cellspacing="0">
									<tr>

										<td id="incomings_cell" style="text-align: center; padding: 0 4px" class="box-item firstcell nowrap">
																						<img src="http://dsen.innogamescdn.com/8.24/20825/graphic/unit/att.png?1bdd4" title="Incoming attacks" style="vertical-align: -2px" alt="" class="" />
											<span id="incomings_amount">0</span>
																					</td>

										<td id="supports_cell" style="text-align: center; padding: 0 4px" class="box-item separate nowrap">
											<a href="">
												<img src="http://dsen.innogamescdn.com/8.24/20825/graphic/command/support.png?90fdb" title="Incoming support" style="vertical-align: -2px" alt="" class="" />
												<span id="supports_amount"></span>
											</a>
										</td>
									</tr>
								</table>
							</td>
						</tr>
						<tr class="newStyleOnly">
							<td class="shadow">
								<div class="leftshadow"> </div>
								<div class="rightshadow"> </div>
							</td>
						</tr>
					</table>
				</td>

			</tr>
		</table>

		
		
		
		
		<div id="script_warning" class="info_box" style="display: none;" >
			The activated scripts may be incompatible with the current game version.<br />
			Should problems still occur, please deactivate or update the scripts.<br />
			If problems still occur, please contact the author of the script. <ul id="script_list"></ul>
		</div>


	    
	    
		<!-- *********************** CONTENT BELOW ************************** -->
		<table align="center" id="contentContainer" width="100%">
	        <tr>
	            <td>
					<table class="content-border" width="100%" cellspacing="0">
	                    <tr>
	                        <td id="inner-border">
								<table class="main" align="left">
	                                <tr>
										<td id="content_value">
										
										
	                               		<table width="100%">
	<tr>
		<td valign="top"><img src="http://dsen.innogamescdn.com/8.24/20825/graphic/big_buildings/place1.png?369e9" title="Rally point" alt="" class="" /></td>
		<td valign="top" width="100%">
			<h2>Rally point (Level 1)</h2>
			On the rally point your fighters meet. Here you can command your armies.
		</td>
	</tr>
</table>

<table class="vis modemenu" width="100%">
	<tr>
		<td  style="min-width: 80px"><a href="/game.php?village=18518&amp;screen=place&amp;mode=command">Commands </a></td>
		<td  style="min-width: 80px"><a href="/game.php?village=18518&amp;screen=place&amp;mode=secrets">Secret </a></td>
		<td  class="selected" style="min-width: 80px"><a href="/game.php?village=18518&amp;screen=place&amp;mode=units">Troops </a></td>
		<td  style="min-width: 80px"><a href="/game.php?village=18518&amp;screen=place&amp;mode=sim">Simulator </a></td>
		<td  style="min-width: 80px"><a href="/game.php?village=18518&amp;screen=place&amp;mode=templates">Troop templates </a></td>
		</tr>
</table>

<h3>Defenses</h3>
<script type="text/javascript">
//<![CDATA[
	$(function(){
		JToggler.init('#units_home input[type="checkbox"]');
	});
//]]>
</script>

<form action="/game.php?village=18518&amp;mode=units&amp;action=command_other&amp;h=e049&amp;screen=place" method="post">
<table id="units_home" class="vis" width="100%">
<tr><th>Origin</th><th style="text-align:center"  width="40"><img src="http://dsen.innogamescdn.com/8.24/20825/graphic/unit/unit_spear.png?48b3b" title="Spear fighter" alt="" class="" /></th><th style="text-align:center"  width="40"><img src="http://dsen.innogamescdn.com/8.24/20825/graphic/unit/unit_sword.png?b389d" title="Swordsman" alt="" class="" /></th><th style="text-align:center"  width="40"><img src="http://dsen.innogamescdn.com/8.24/20825/graphic/unit/unit_axe.png?51d94" title="Axeman" alt="" class="" /></th><th style="text-align:center"  width="40"><img src="http://dsen.innogamescdn.com/8.24/20825/graphic/unit/unit_spy.png?eb866" title="Scout" alt="" class="" /></th><th style="text-align:center"  width="40"><img src="http://dsen.innogamescdn.com/8.24/20825/graphic/unit/unit_light.png?2d86d" title="Light cavalry" alt="" class="" /></th><th style="text-align:center"  width="40"><img src="http://dsen.innogamescdn.com/8.24/20825/graphic/unit/unit_heavy.png?a83c9" title="Heavy cavalry" alt="" class="" /></th><th style="text-align:center"  width="40"><img src="http://dsen.innogamescdn.com/8.24/20825/graphic/unit/unit_ram.png?2003e" title="Ram" alt="" class="" /></th><th style="text-align:center"  width="40"><img src="http://dsen.innogamescdn.com/8.24/20825/graphic/unit/unit_catapult.png?5659c" title="Catapult" alt="" class="" /></th><th style="text-align:center"  width="40"><img src="http://dsen.innogamescdn.com/8.24/20825/graphic/unit/unit_snob.png?0019c" title="Nobleman" alt="" class="" /></th><th style="text-align:center"  width="40"><img src="http://dsen.innogamescdn.com/8.24/20825/graphic/unit/unit_militia.png?ff93f" title="Militia" alt="" class="" /></th></tr>
<tr>
	<td>From this village</td>
	<td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item'>10</td><td style="text-align:center"  class='unit-item'>55</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td>
</tr>
<tr>
	<th>Total</th>
	<th style="text-align:center"  class='unit-item hidden'>0</th><th style="text-align:center"  class='unit-item hidden'>0</th><th style="text-align:center"  class='unit-item'>10</th><th style="text-align:center"  class='unit-item'>55</th><th style="text-align:center"  class='unit-item hidden'>0</th><th style="text-align:center"  class='unit-item hidden'>0</th><th style="text-align:center"  class='unit-item hidden'>0</th><th style="text-align:center"  class='unit-item hidden'>0</th><th style="text-align:center"  class='unit-item hidden'>0</th><th style="text-align:center"  class='unit-item hidden'>0</th>
</tr>
</table>


</form><br style="clear:both;" />
<h3>Troops in transit</h3>


<table id="units_transit" style="width:100%" class="vis groupcols">
<tr>
	<th width="320">Village</th>
	<th style="text-align:center"  width="auto"><img src="http://dsen.innogamescdn.com/8.24/20825/graphic/unit/unit_spear.png?48b3b" title="Spear fighter" alt="" class="" /></th><th style="text-align:center"  width="auto"><img src="http://dsen.innogamescdn.com/8.24/20825/graphic/unit/unit_sword.png?b389d" title="Swordsman" alt="" class="" /></th><th style="text-align:center"  width="auto"><img src="http://dsen.innogamescdn.com/8.24/20825/graphic/unit/unit_axe.png?51d94" title="Axeman" alt="" class="" /></th><th style="text-align:center"  width="auto"><img src="http://dsen.innogamescdn.com/8.24/20825/graphic/unit/unit_spy.png?eb866" title="Scout" alt="" class="" /></th><th style="text-align:center"  width="auto"><img src="http://dsen.innogamescdn.com/8.24/20825/graphic/unit/unit_light.png?2d86d" title="Light cavalry" alt="" class="" /></th><th style="text-align:center"  width="auto"><img src="http://dsen.innogamescdn.com/8.24/20825/graphic/unit/unit_heavy.png?a83c9" title="Heavy cavalry" alt="" class="" /></th><th style="text-align:center"  width="auto"><img src="http://dsen.innogamescdn.com/8.24/20825/graphic/unit/unit_ram.png?2003e" title="Ram" alt="" class="" /></th><th style="text-align:center"  width="auto"><img src="http://dsen.innogamescdn.com/8.24/20825/graphic/unit/unit_catapult.png?5659c" title="Catapult" alt="" class="" /></th><th style="text-align:center"  width="auto"><img src="http://dsen.innogamescdn.com/8.24/20825/graphic/unit/unit_snob.png?0019c" title="Nobleman" alt="" class="" /></th>
			<th>Cancel</th>
	</tr>
	<tr>
		<td>
							<img src="http://dsen.innogamescdn.com/8.24/20825/graphic/command/return.png?f546e" title="Returning attack" alt="" class="tooltip" />
			            <a href="/game.php?village=18518&amp;id=22820&amp;screen=info_village" >Amnks village (361|508) K53</a>
        </td>
		<td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item'>11</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td>
					<td></td>
			</tr>
	<tr>
		<td>
							<img src="http://dsen.innogamescdn.com/8.24/20825/graphic/command/return.png?f546e" title="Returning attack" alt="" class="tooltip" />
			            <a href="/game.php?village=18518&amp;id=21912&amp;screen=info_village" >anasemo s village (362|506) K53</a>
        </td>
		<td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item'>12</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td>
					<td></td>
			</tr>
	<tr>
		<td>
							<img src="http://dsen.innogamescdn.com/8.24/20825/graphic/command/return.png?f546e" title="Returning attack" alt="" class="tooltip" />
			            <a href="/game.php?village=18518&amp;id=20024&amp;screen=info_village" >Barbarian village (370|521) K53</a>
        </td>
		<td style="text-align:center"  class='unit-item'>9</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item'>52</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td>
					<td></td>
			</tr>
	<tr>
		<td>
							<img src="http://dsen.innogamescdn.com/8.24/20825/graphic/command/return.png?f546e" title="Returning attack" alt="" class="tooltip" />
			            <a href="/game.php?village=18518&amp;id=19850&amp;screen=info_village" >Barbarian village (370|515) K53</a>
        </td>
		<td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item'>24</td><td style="text-align:center"  class='unit-item'>55</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td>
					<td></td>
			</tr>
	<tr>
		<td>
							<img src="http://dsen.innogamescdn.com/8.24/20825/graphic/command/return.png?f546e" title="Returning attack" alt="" class="tooltip" />
			            <a href="/game.php?village=18518&amp;id=22321&amp;screen=info_village" >Bonus village (363|519) K53</a>
        </td>
		<td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item'>10</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td>
					<td></td>
			</tr>
	<tr>
		<td>
							<img src="http://dsen.innogamescdn.com/8.24/20825/graphic/command/attack_small.png?7aac8" title="Small attack (1-1000 troops)" alt="" class="tooltip" />
			            <a href="/game.php?village=18518&amp;id=21478&amp;screen=info_village" >Bonus village (366|511) K53</a>
        </td>
		<td style="text-align:center"  class='unit-item'>14</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item'>45</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td>
					<td></td>
			</tr>
	<tr>
		<td>
							<img src="http://dsen.innogamescdn.com/8.24/20825/graphic/command/return.png?f546e" title="Returning attack" alt="" class="tooltip" />
			            <a href="/game.php?village=18518&amp;id=23359&amp;screen=info_village" >Bonus village (362|521) K53</a>
        </td>
		<td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item'>10</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td>
					<td></td>
			</tr>
	<tr>
		<td>
							<img src="http://dsen.innogamescdn.com/8.24/20825/graphic/command/return.png?f546e" title="Returning attack" alt="" class="tooltip" />
			            <a href="/game.php?village=18518&amp;id=24163&amp;screen=info_village" >Bonus village (361|517) K53</a>
        </td>
		<td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item'>10</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td>
					<td></td>
			</tr>
	<tr>
		<td>
							<img src="http://dsen.innogamescdn.com/8.24/20825/graphic/command/return.png?f546e" title="Returning attack" alt="" class="tooltip" />
			            <a href="/game.php?village=18518&amp;id=18571&amp;screen=info_village" >Hernandez713s village (372|509) K53</a>
        </td>
		<td style="text-align:center"  class='unit-item'>14</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item'>58</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td>
					<td></td>
			</tr>
	<tr>
		<td>
							<img src="http://dsen.innogamescdn.com/8.24/20825/graphic/command/return.png?f546e" title="Returning attack" alt="" class="tooltip" />
			            <a href="/game.php?village=18518&amp;id=17004&amp;screen=info_village" >King Zygens villa (377|518) K53</a>
        </td>
		<td style="text-align:center"  class='unit-item'>9</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item'>52</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td>
					<td></td>
			</tr>
	<tr>
		<td>
							<img src="http://dsen.innogamescdn.com/8.24/20825/graphic/command/attack_small.png?7aac8" title="Small attack (1-1000 troops)" alt="" class="tooltip" />
			            <a href="/game.php?village=18518&amp;id=18563&amp;screen=info_village" >NOBLESSE (371|510) K53</a>
        </td>
		<td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item'>5</td><td style="text-align:center"  class='unit-item'>14</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td>
					<td><a href="/game.php?village=18518&amp;action=cancel&amp;h=e049&amp;mode=units&amp;redirect=0&amp;id=871440191&amp;screen=place">Cancel</a></td>
			</tr>
	<tr>
		<td>
							<img src="http://dsen.innogamescdn.com/8.24/20825/graphic/command/return.png?f546e" title="Returning attack" alt="" class="tooltip" />
			            <a href="/game.php?village=18518&amp;id=18563&amp;screen=info_village" >NOBLESSE (371|510) K53</a>
        </td>
		<td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item'>25</td><td style="text-align:center"  class='unit-item'>54</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td>
					<td></td>
			</tr>
	<tr>
		<td>
							<img src="http://dsen.innogamescdn.com/8.24/20825/graphic/command/attack_small.png?7aac8" title="Small attack (1-1000 troops)" alt="" class="tooltip" />
			            <a href="/game.php?village=18518&amp;id=19973&amp;screen=info_village" >readysss village (365|511) K53</a>
        </td>
		<td style="text-align:center"  class='unit-item'>10</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item'>55</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td>
					<td></td>
			</tr>
	<tr>
		<td>
							<img src="http://dsen.innogamescdn.com/8.24/20825/graphic/command/attack_small.png?7aac8" title="Small attack (1-1000 troops)" alt="" class="tooltip" />
			            <a href="/game.php?village=18518&amp;id=19694&amp;screen=info_village" >secret (369|505) K53</a>
        </td>
		<td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item'>12</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td>
					<td></td>
			</tr>
	<tr>
		<td>
							<img src="http://dsen.innogamescdn.com/8.24/20825/graphic/command/attack_small.png?7aac8" title="Small attack (1-1000 troops)" alt="" class="tooltip" />
			            <a href="/game.php?village=18518&amp;id=18892&amp;screen=info_village" >TheHugeDanes village (368|509) K53</a>
        </td>
		<td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item'>11</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td>
					<td></td>
			</tr>
	<tr>
		<td>
							<img src="http://dsen.innogamescdn.com/8.24/20825/graphic/command/return.png?f546e" title="Returning attack" alt="" class="tooltip" />
			            <a href="/game.php?village=18518&amp;id=18892&amp;screen=info_village" >TheHugeDanes village (368|509) K53</a>
        </td>
		<td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item'>16</td><td style="text-align:center"  class='unit-item'>42</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td>
					<td></td>
			</tr>
	<tr>
		<td>
							<img src="http://dsen.innogamescdn.com/8.24/20825/graphic/command/return.png?f546e" title="Returning attack" alt="" class="tooltip" />
			            <a href="/game.php?village=18518&amp;id=21634&amp;screen=info_village" >Woe is Me (362|514) K53</a>
        </td>
		<td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item'>10</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td><td style="text-align:center"  class='unit-item hidden'>0</td>
					<td></td>
			</tr>
</table>

	                               		</td>
									</tr>
								</table>
							</td>
						</tr>
					</table>
				</td>
			</tr>
		</table>

		<p class="server_info">
			Server time: <span id="serverTime">2:13:50</span> <span id="serverDate">21/06/2014</span>
			<span id="dev_console" style="display: none"><b>|</b> <a href="?screen=74:72:69:62:61:6c:77:61:72:73">developer console</a></span>
					</p>

	</td>
	<td class="bg_right" id="SkyScraperAdCell">
		<div class="bg_right"> </div>
		<div id="SkyScraperAd"><iframe id='abfb7040' name='abfb7040' src='http://openx.innogames.de/delivery/afr.php?zoneid=57&amp;cb=INSERT_RANDOM_NUMBER_HERE' frameborder='0' scrolling='no' height='600'><a href='http://openx.innogames.de/delivery/ck.php?n=af620030&amp;cb=INSERT_RANDOM_NUMBER_HERE' target='_blank'><img src='http://openx.innogames.de/delivery/avw.php?zoneid=57&amp;cb=INSERT_RANDOM_NUMBER_HERE&amp;n=af620030' border='0' alt='' /></a></iframe></div>	</td>
</tr>

						<tr>
				<td class="bg_leftborder"> </td>
				<td></td>
				<td class="bg_rightborder"> </td>
			</tr>
			<tr class="newStyleOnly">
				<td class="bg_bottomleft">&nbsp;</td>
				<td class="bg_bottomcenter">&nbsp;</td>
				<td class="bg_bottomright">&nbsp;</td>
			</tr>
							<tr><td colspan="3" align="center"><div id="AdBottom"></div></td></tr>
						</table><!-- .main_layout -->
					
<script type="text/javascript">
//<![CDATA[
	$(document).ready(function() { 
		Timing.init(1403313230.6598);
	});
//]]>
</script>

<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-1897727-3']);
  _gaq.push(['_trackPageview']);
  _gaq.push(['_gat._anonymizeIp']);


  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(ga);
  })();

</script>

		
				<div id="world_selection_clicktrap" class="evt-world-selection-toggle">
		</div>
		<div id="world_selection_popup">
			<div class="servers-list-top"></div>
			<div id="servers-list-block">
			
			</div>
			<div class="servers-list-bottom"></div>
		</div>
		
		<div id="footer">
			<div id="linkContainer">
								<a href="#" class="world_button_active evt-world-selection-toggle">World 75</a>
								<a href="http://forum.tribalwars.net/index.php" class="footer-link" target="_blank">Forum</a>
				&nbsp;-&nbsp;
				<a href="http://help.tribalwars.net" class="footer-link" target="_blank">Help</a>
												&nbsp;-&nbsp;
				<a href="/game.php?village=18518&amp;mode=ticket&amp;screen=settings" class="footer-link" target="_blank">Support</a>
													&nbsp;-&nbsp;
					<a href="/game.php?village=18518&amp;mode=ref&amp;source=bottom_menu&amp;screen=settings" class="footer-link">Invite players</a>
				                				&nbsp;-&nbsp;
				<a href="/game.php?village=18518&amp;screen=memo" class="footer-link">Notebook</a>
                				&nbsp;-&nbsp;
				<a href="/game.php?village=18518&amp;action=logout&amp;h=e049&amp;screen=" target="_top" class="footer-link">Log out</a>
			</div>
		</div>
		






<script>
	$(document).ready(function() {
			WorldSwitch.init();
		WorldSwitch.worldsURL = '/game.php?village=18518&ajax=world_switch&screen=api';
	
			HotKeys.init();
	
	
	
	});
</script>

</body>
</html>
"""

m = re.search("<tr>\s*<td>From this village</td>\s*(.+)\s*</tr>", text)
if m:
	units = m.group(1)
	listy = re.findall(r'\d+', units)
else:
	print "missed"

spears = listy[0]
axes = listy[2]
lc = listy[4]

print spears,axes,lc

