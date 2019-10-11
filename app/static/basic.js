function react(event) {
    let value = $("#search-box input")[0].value;

    fillAvanzata(value);

    value = value.toLowerCase(); // to support case insensitive matching


    if (value.length > 0) {
        if ("firenze".indexOf(value) === 0) {
            showFirenze();
        } else if ("cinema".indexOf(value) === 0) {
            showCinema();
        } else {
            hideEverything();
        }
    } else {
        hideEverything();
    }
}

function fillAvanzata(value) {
    // put the text of the search after "ricerca avanzata"
    $(".searchString").html(value)
}

function showFirenze() {
    $("#search-result").show();
    $("#firenze").show();
     $("#cinema").hide();
}

function showCinema() {
    $("#search-result").show();
    $("#cinema").show();
     $("#firenze").hide();
}

function hideEverything() {
    $("#firenze").hide();
    $("#cinema").hide();
    $("#search-result").hide();
}


$("#search-box > form").keyup(react);
