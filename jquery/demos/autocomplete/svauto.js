console.log('sv--');
requirejs(['jquery'], function( $ ) {
    console.log( $ ) // OK

    $(document).ready(function(){
    var people = ['Peter Bishop', 'Nicholas Brody', 'Gregory House', 'Hank Lawson', 'Tyrion Lannister', 'Nucky Thompson'];
    var cache = {};
    var drew = false;
     var results ;
    $('#svsearch').on('keyup', function(event){
    	 var query = $('#svsearch').val();
    	 if(query in cache){
    	 	results = cache[query];
    	 	console.log(results);

    	 }else{
    	  results =	$.grep(people, function(item){
    	 		var o = item.search( RegExp(query, "i"));
    	 		console.log(o);
    	 		return item.search( RegExp(query, "i")) != -1 ;
    	 	})
    	 }
    	 console.log(results);
    	 cache[query] = results;

    	 if(drew ===false){
    	 	$('#svsearch').after('<ul class="svbox" id="res"></ul>');
    	 	drew = true;

    	 	$('#res').on('click', 'li', function(){
    	 		 console.log($(this));
    	 		//sv bind click elements to results
    	 		$('#svsearch').val($(this).text());
    	 		$('#res').empty();
    	 	})
    	 }else{
    	 	//sv remove old resilts
    	 	$('#res').empty();
    	 }

    	 for(term in results){
    	 	$('#res').append('<li>' + results[term]+' </li>')
    	 }
    })
    /*
    
    $("#svsearch").on("keyup", function(event){
        var query = $("#search").val()
 
        if($("#svsearch").val().length > 2){
            
            //Check if we've searched for this term before
            if(query in cache){
                results = cache[query];
            }
            else{
                //Case insensitive search for our people array
                var results = $.grep(people, function(item){
                    return item.search(RegExp(query, "i")) != -1;
                });
                
                //Add results to cache
                cache[query] = results;
            }
        }
    });*/
});
});

