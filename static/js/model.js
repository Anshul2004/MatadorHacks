function run(input) {
    return [1/(1+1/Math.exp((-2.7477240562438965+6.965540409088135*1/(1+1/Math.exp((0.7144330143928528-0.027614159509539604*input['0']-0.019645189866423607*input['1']-0.04887250065803528*input['2']+3.2339110374450684*input['3']-0.309761106967926*input['4']+0.20992334187030792*input['5']-0.40758973360061646*input['6']+0.08821433782577515*input['7']-0.09435424208641052*input['8']+0.030927134677767754*input['9']-0.2860075533390045*input['10']-0.0027878007385879755*input['11']+0.4985412359237671*input['12']-0.21282817423343658*input['13']+0.13050730526447296*input['14']-3.1835367679595947*input['15']+0.5363516807556152*input['16']-0.1804552972316742*input['17']+0.4141230285167694*input['18']+0.04024220630526543*input['19']-0.04018301144242287*input['20']+0.1571374386548996*input['21']+0.10251069068908691*input['22']+0.15321946144104004*input['23'])))-4.468423843383789*1/(1+1/Math.exp((-0.06084614619612694-0.5082372426986694*input['0']-0.13412240147590637*input['1']-0.7893728613853455*input['2']+0.2164117991924286*input['3']-0.1865682452917099*input['4']+0.5739727020263672*input['5']+0.1751495599746704*input['6']-0.03578329086303711*input['7']-0.03555266931653023*input['8']+0.22258779406547546*input['9']+0.3628033697605133*input['10']+0.8679731488227844*input['11']-0.3151778280735016*input['12']-1.0764371156692505*input['13']-0.1992199420928955*input['14']-0.13331641256809235*input['15']+0.37998077273368835*input['16']-0.016026536002755165*input['17']+0.9715308547019958*input['18']+0.09748804569244385*input['19']+0.33781519532203674*input['20']+0.13864801824092865*input['21']+0.06783512979745865*input['22']+0.12268407642841339*input['23'])))+8.531193733215332*1/(1+1/Math.exp((0.6803730726242065-0.18920129537582397*input['0']+3.8365120887756348*input['1']-0.11560331284999847*input['2']-0.5100541710853577*input['3']+0.0689074844121933*input['4']+0.3882701098918915*input['5']-0.01661907695233822*input['6']+0.2703011929988861*input['7']+0.027967844158411026*input['8']-0.03784995153546333*input['9']-0.06654266268014908*input['10']+0.1903698742389679*input['11']+0.3552893102169037*input['12']-3.7458620071411133*input['13']+0.02732972986996174*input['14']+0.7325836420059204*input['15']+0.10684987157583237*input['16']-0.6153586506843567*input['17']+0.31650713086128235*input['18']-0.12737581133842468*input['19']-0.03871584311127663*input['20']-0.04672643542289734*input['21']+0.12377764284610748*input['22']-0.08171097934246063*input['23'])))-6.402121543884277*1/(1+1/Math.exp((-1.13316011428833-0.17164497077465057*input['0']+0.24296823143959045*input['1']-1.2991318702697754*input['2']+0.5838591456413269*input['3']-3.246587038040161*input['4']-0.06799974292516708*input['5']-0.3178166449069977*input['6']+0.058286748826503754*input['7']-0.021189523860812187*input['8']-0.48536473512649536*input['9']-0.0460241436958313*input['10']-0.17261338233947754*input['11']-0.34172460436820984*input['12']+0.08265108615159988*input['13']+1.4197434186935425*input['14']-0.27589988708496094*input['15']+3.0897650718688965*input['16']-0.09727424383163452*input['17']+0.044714849442243576*input['18']-0.18750494718551636*input['19']-0.23799070715904236*input['20']+0.20213904976844788*input['21']+0.18784639239311218*input['22']+0.10484308749437332*input['23'])))-6.155101776123047*1/(1+1/Math.exp((-1.1760213375091553-0.2021983116865158*input['0']+1.543399691581726*input['1']+0.9258391857147217*input['2']+0.9048910140991211*input['3']+1.0420113801956177*input['4']+0.30083245038986206*input['5']-1.0988529920578003*input['6']-0.05257901921868324*input['7']-0.25100165605545044*input['8']+0.13187234103679657*input['9']-0.15700814127922058*input['10']-0.09559683501720428*input['11']+1.0417931079864502*input['12']-1.3079248666763306*input['13']-0.743431031703949*input['14']-1.0206066370010376*input['15']-0.8032780885696411*input['16']-0.5141628384590149*input['17']+0.9067891240119934*input['18']-0.09642058610916138*input['19']+0.08440402895212173*input['20']-0.012004072777926922*input['21']-0.27810487151145935*input['22']-0.2070242017507553*input['23']))))))];
};

function convertToNumberArray(word1, word2){
    const alphabet = "qwertyuiopasdfghjklzxcvbnm";

    word1 = word1.toLowerCase();
    word2 = word2.toLowerCase();

    word1 = word1.replace(/\s/g, '');
    word2 = word2.replace(/\s/g, '');

    if(word1.length > 12){
        word1 = word1.substring(0, 12);
    }
    else if(word1.length < 12){
        const difference = 12 - word1.length;
        for(j = 0; j < difference; j++){
            word1 += alphabet[Math.floor(Math.random()*alphabet.length)];
        }
    }
    if(word2.length > 12){
        word2 = word2.substring(0, 12);
    }
    else if(word2.length < 12){
        const difference = 12 - word2.length;
        for(j = 0; j < difference; j++){
            word2 += alphabet[Math.floor(Math.random()*alphabet.length)];
        }
    }
    
    var array = [];

    for(j = 0; j < word1.length; j++){
        for(k = 0; k < alphabet.length; k++){
            if(alphabet[k] == word1[j]){
                array.push(k);
            }
        }
    }
    for(j = 0; j < word2.length; j++){
        for(k = 0; k < alphabet.length; k++){
            if(alphabet[k] == word2[j]){
                array.push(k);
            }
        }
    }

    return array;
}

function find(units){
    var input = document.getElementById("inputted").value;
    var array = []
    var dictionary = {};
    for(i = 0; i < units.length; i++){
        const val = run(convertToNumberArray(input, units[i]))[0];
        array.push(val);
        dictionary[val] = units[i];
    }
    array = sort(array);
    var finalArray = [];
    for(i = 0; i < array.length; i++){
        finalArray.push(dictionary[array[i]]);
    }

    for(l = 0; l < finalArray.length; l++){
        var x = String(document.getElementById(finalArray[l].replace(/\s/g, '-')).style.height);
        console.log(x);
        document.getElementById(finalArray[l].replace(/\s/g, '-')).style.position = "absolute";
        document.getElementById(finalArray[l].replace(/\s/g, '-')).style.marginTop = String((l*70)+5)+"%";
        document.getElementById(finalArray[l].replace(/\s/g, '-')).style.width = "86%";
        document.getElementById(finalArray[l].replace(/\s/g, '-')).style.marginLeft = "-45%";
    }

    document.getElementById("footer").style.marginTop=String(finalArray.length*70)+"%";

    return finalArray;
}

function sort(points) {
    points.sort(function(a, b){return b-a});
    return points;
}