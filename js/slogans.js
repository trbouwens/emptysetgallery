const slogans = ["Spend money.  Live better.", "Finger-lickin' good", "It's not empty unless it's {Empty Set}", "Brought to you by {Empty Set}", "Quality Art.  Quality Prices.", "Where art goes to die.", "Better artists.  Better art.", "Nobody out-arts the art.", "No."];
document.getElementById("slogan").innerText = slogans[Math.floor(Math.random() * slogans.length)];
