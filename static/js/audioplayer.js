window.onload = function () {

	var songlist = []
	var playing = false;
	var s = Snap("#svg"); // This will use an existing svg element (not a div)
	var selectedListItem = null;
	var outerRect = s.rect(10, 10, 400, 379, 25, 25);
	outerRect.attr('fill', '#1A3133');

	var titleText = s.text(50, 50, "Was A Time");
	titleText.attr({ fill: '#4CDCF5', "font-size": '24px' });

	var artistText = s.text(50, 75, "Anthony D'Amato");
	artistText.attr({ fill: '#4CDCF5', "font-size": '12px' });
        var innerPlayButton = s.polygon([92,115,112,125,92,135]);
//	var innerPauseButtonLeft = s.rect(92,115,5,20);	

	var playButton = s.circle(100, 125, 20);
	playButton.attr({stroke: '#0298B3','strokeWidth':1,fill:'#1A3133'})
	//var innerPlayButton = s.polygon([92,115,112,125,92,135]);
        var innerPauseButtonLeft = s.rect(94,115,5,20);
	var innerPauseButtonRight = s.rect(102,115,5,20);
	var innerPauseButton = s.group(innerPauseButtonRight,innerPauseButtonLeft);
	innerPauseButton.attr({fill:'#4CDCF5',pointerEvents:"none",opacity:0});	
	innerPlayButton.attr({fill: '#4CDCF5',pointerEvents:"none",opacity:1});
	
	var backButton = s.circle(55,125,18);
	backButton.attr({stroke: '#0298B3','strokeWidth':1,fill:'#1A3133'})

	var innerBackButtonTriangle = s.polygon([62,118,52,125,62,132]);
	var innerBackButtonRect = s.rect(49,118,4,14);
	var backButtonInnerGroup = s.group(innerBackButtonTriangle,innerBackButtonRect);
	backButtonInnerGroup.attr({fill:'#4CDCF5',pointerEvents:"none"});

	var nextButton = s.circle(145,125,18);
        nextButton.attr({stroke: '#0298B3','strokeWidth':1,fill:'#1A3133'})

	var innerNextButtonTriangle = s.polygon([138,118,148,125,138,132]);
	var innerNextButtonRect = s.rect(148,118,4,14);
	var nextButtonInnerGroup = s.group(innerNextButtonTriangle,innerNextButtonRect);
	nextButtonInnerGroup.attr({fill:'#4CDCF5',pointerEvents:"none"});

	var playGroup = s.group(playButton,innerPlayButton,innerPauseButton);
	playGroup.click(function () { playButtonClick()});
	//playGroup.hover(buttonHoverIn,buttonHoverOut);
		

	var songTimeline = s.rect(175,122,200,6);
	songTimeline.attr({stroke:'#0298B3','strokeWidth':1})
	var curPos  = s.rect(175,122,10,6);
	curPos.attr({fill:'#4CDCF5'})

	var buttonHoverIn = function(event){
		var obj = Snap(event.target);
		console.log(obj.node.fill);
		obj.attr({fill:'#0298B3'})
		console.log(obj);
	}

	var buttonHoverOut = function(event){
		var obj = Snap(event.target);
		obj.attr({fill:'#1A3133'});
		console.log(obj);
	}

	playButton.hover(buttonHoverIn,buttonHoverOut);
        backButton.hover(buttonHoverIn,buttonHoverOut);
        nextButton.hover(buttonHoverIn,buttonHoverOut);
	var playButtonClick = function () {
		console.log("hello")
		var audioBlock = document.getElementById('peaks-audio');
                
		if (playing === false) {
                        playing = true;
                        innerPlayButton.attr({opacity:0});
                        innerPauseButton.attr({opacity:1});
                	audioBlock.play();
		}
                else {
                        playing = false;
                        innerPlayButton.attr({opacity:1});
                        innerPauseButton.attr({opacity:0});
                	audioBlock.pause();
		}

	}
    
	var makeSongList = function () {
		$.ajax({
			type: "GET",
			url: "/returnPlaylist",
			data: {}
		}).done(function (o) {
			var index = 0;
			for(var i = 0;i < o.songlist.length;i++){
				var obj = o.songlist[i];
				songlist[i] = {name: obj[0],artist: obj[1],file:obj[2]};
			}
			drawSongList();
        	});
	}

	makeSongList();
	var drawSongList = function(){
		for(var i = 0;i < songlist.length;i++) {
			var song = songlist[i];
			var yPosBottom = 150 + i*30 + 25;
			var songRect = s.rect(25,150 + i*32 ,370,30);
			songRect.attr({fill:'#1A3133'})
			var songText = s.text(35,150+i*30+25,(i+1) + ".  "  + songlist[i].name);
			songRect.node.playId = i;
			songText.attr({fill: '#4CDCF5',pointerEvents:"none"});
			songText.node.playId = i;
			var pathString = "M25 " + yPosBottom + "L395 " + yPosBottom;
				
			
			var songGroup = s.group(songRect,songText);
			
			songGroup.click(clickSongBox);	
			var bottomLine = s.rect(25,yPosBottom + 5,370,1)
			bottomLine.attr({fill:'#4CDCF5'});
		}
	}

	var clickSongBox = function(event){
		var obj = Snap(event.target).node;	
		var index = obj.playId;
		var audioBlock = document.getElementById('peaks-audio');		
		var sourceBlock = document.getElementById('audio-source');
		sourceBlock.src = "../static/files/music/" + songlist[index].file;
		audioBlock.load();	
		titleText.node.textContent = songlist[index].name;
		artistText.node.textContent = songlist[index].artist;
		Snap(event.target).attr({fill:'#0298B3'});	
		console.log(Snap(event.target));
		if (selectedListItem !== null) {
			selectedListItem.attr({fill:'#1A3133'});
		}
		selectedListItem = Snap(event.target);
	}	


}

$('#idj-play-button').click(function () {
    document.getElementById('peaks-audio').play();
    $('#idj-play-button').addClass('hide');
    $('#idj-pause-button').removeClass('hide');

});

$('#idj-pause-button').click(function () {
    document.getElementById('peaks-audio').pause();
    $('#idj-pause-button').addClass('hide');
    $('#idj-play-button').removeClass('hide');
});

$('#peaks-audio').on('ended', function () {
    $('#idj-pause-button').addClass('hide');
    $('#idj-play-button').removeClass('hide');
    $('#peaks-audio').load();
});
