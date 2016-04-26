window.onload = function () {



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
            // do something
		console.log(o);
        });
    }
    makeSongList();
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
