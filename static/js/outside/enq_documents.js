
// 
// Documents
// 
// 

oo.enq.docs.update = function( event, filters ){

	oo.log("[oo.enq.docs.update]");

	var	docs = d3.select('#documents ul'),
		counter = d3.select('#counter span.docNumber')
		container = d3.select('#counter p'),
		meter = 0;

	var items = docs.selectAll('li').each(function(d, i) {
		item = d3.select(this);
		item.attr('data-status-old', item.attr('data-status'));
	}); // Copy new status to old status

	for ( var i in oo.filt.data ) {
		var item = docs.select('li[data-id="' + oo.filt.data[i].id + '"]');
		if ( oo.filt.data[ i ].filtered ) {
			item.attr('data-status', 'active');
			meter++;
		} else {
			item.attr('data-status', 'inactive');	
		}
	} // Set active


	items.each(function() {

		var item = d3.select(this),
			oldStatus = item.attr('data-status-old'),
			newStatus = item.attr('data-status');

		if ( oldStatus == 'active' && newStatus == 'inactive' ) {
			item.transition()
				.duration(1000)
				.style('opacity', '0')
				.style('height', '0px');
		} else if ( oldStatus == 'inactive' && newStatus == 'active' ) {
			item.transition()
				.duration(1000)
				.style('opacity', '1')
				.style('height', '22px');
		} 
	})

	var delay = 500;

	container.transition()
		.duration(delay)
		.style('margin-top', '30px');

	counter.transition()
		.duration(1)
		.delay(delay)
		.text(meter);
		
	container.transition()
		.delay(delay + 300)
		.duration(1000)
		.style('margin-top', '0px');

};

oo.enq.docs.init = function ( objects ){

	oo.filt.on( oo.filt.events.change, oo.enq.docs.update );

	d3.select("#reset")
        .on("click", oo.filt.clean );

	var counter = d3.select('#counter span.docNumber'),
		docs = d3.select('#documents ul'),
		container = d3.select('#counter p');

	var map = objects.sort(function (a, b){ 
		return a.title > b.title ? 1 : a.title < b.title ? -1 : 0
	}) // Sorting

	var li = docs.selectAll("li")
		.data(map)
		.enter().append("li")
		.attr('class', 'active')
		.attr('data-id', function(d) { return d.id; })
		.attr('data-status', 'active')
		
		.html(function(d) {
			oo.log(d)
			
			var string = d.title.split('_').join(' ').split('/').join(' ') + '<br/>';
			
			if (typeof d.type != 'undefined' ) string += '<i>'+d.type+'</i>' 
			if (typeof d.phases[0].phase != 'undefined' ) string += '<i>'+d.phases[0].phase+'</i>' 
			if (typeof d.categories[0].category != 'undefined' ) string += '<i>'+d.categories[0].category+'</i>' 
			if ( d.articles.length != 0 ) string += '<i>'+d.articles[0].article+'</i>' 

			return string;
		})

		.on('click', function(d, i) {
			oo.log('this', this)
			oo.log('id', d3.select(this).attr('data-id'))
			window.open( oo.api.urlfactory( oo.urls.get_document, d3.select(this).attr('data-id') ), '_blank');
		});

	counter.html(li[0].length);

	container.transition()
		.duration(500)
		.style('margin-top', '0px');
	
	$('#documents-inner').slimScroll({height:493});
};

