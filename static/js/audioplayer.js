window.onload = function () {

	var songlist = []

    var s = Snap("#svg"); // This will use an existing svg element (not a div)

    var outerRect = s.rect(10, 10, 400, 379, 25, 25);
    outerRect.attr('fill', '#1A3133');

    var titleText = s.text(50, 50, "Was A Time");
    titleText.attr({ fill: '#4CDCF5', "font-size": '24px' });

    var artistText = s.text(50, 75, "Anthony D'Amato");
    artistText.attr({ fill: '#4CDCF5', "font-size": '12px' });

    var playButton = s.circle(100, 125, 20);

    playButton.click(function () { playButtonClick()});

    var playButtonClick = function () {
        console.log("hello")
        document.getElementById('peaks-audio').play();
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
			var songRect = s.rect(25,150 + i*30,370,30);
			var songText = s.text(35,150+i*30+25,(i+1) + ".  "  + songlist[i].name);
			songRect.node.playId = i;
			songText.attr({fill: '#4CDCF5'});
			songText.node.playId = i;
			var songGroup = s.group(songRect,songText);
			
			songGroup.click(clickSongBox);
			
		}
	}

	var clickSongBox = function(event){
		var obj = Snap(event.target).node;	
		var index = obj.playId;
		var audioBlock = document.getElementById('peaks-audio');		
		var sourceBlock = document.getElementById('audio-source');
		console.log(sourceBlock);
		sourceBlock.src = "../static/files/music/" + songlist[index].file;
		audioBlock.load()
		//audioBlock.play();
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
