
"use strict"

var dezSettingsOptions = {};

function getUrlParams(dParam) 
	{
		var dPageURL = window.location.search.substring(1),
			dURLVariables = dPageURL.split('&'),
			dParameterName,
			i;

		for (i = 0; i < dURLVariables.length; i++) {
			dParameterName = dURLVariables[i].split('=');

			if (dParameterName[0] === dParam) {
				return dParameterName[1] === undefined ? true : decodeURIComponent(dParameterName[1]);
			}
		}
	}

(function($) {
	
	"use strict"
	
	/* var direction =  getUrlParams('dir');
	
	if(direction == 'rtl')
	{
        direction = 'rtl'; 
    }else{
        direction = 'ltr'; 
    } */
	
	dezSettingsOptions = {
			typography: "poppins",
			version: getCookie('theme-mode') || 'light',
			layout: "vertical",
			primary: "color_1",
			headerBg: "color_1",
			navheaderBg: "color_1",
			sidebarBg: "color_1",
			sidebarStyle: "full",
			sidebarPosition: "fixed",
			headerPosition: "fixed",
			containerLayout: "full",
		};

	
	
	
	new dezSettings(dezSettingsOptions); 

	jQuery(window).on('resize',function(){
        /*Check container layout on resize */
		///alert(dezSettingsOptions.primary);
        dezSettingsOptions.containerLayout = $('#container_layout').val();
        /*Check container layout on resize END */
        
		new dezSettings(dezSettingsOptions); 
	});
	
})(jQuery);


let btn_switch_theme_dark = document.querySelector('[btn-switch-theme][theme="dark"]')
let btn_switch_theme_light = document.querySelector('[btn-switch-theme][theme="light"]')

btn_switch_theme_dark.addEventListener('click', function () {
    btn_switch_theme_dark.classList.add('d-none')
    btn_switch_theme_light.classList.remove('d-none')
    set_theme('dark')
})

btn_switch_theme_light.addEventListener('click', function () {
    btn_switch_theme_light.classList.add('d-none')
    btn_switch_theme_dark.classList.remove('d-none')
    set_theme('light')
})

function set_theme(theme) {
    dezSettingsOptions = {
        version: theme,
    }
    new dezSettings(dezSettingsOptions);
	setCookie('theme-mode', theme)
}

if ((getCookie('theme-mode') || 'light') == 'light'){

	btn_switch_theme_light.click()
}else{
	btn_switch_theme_dark.click()
}