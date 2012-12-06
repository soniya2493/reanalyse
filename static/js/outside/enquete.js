var oo = oo || {};

oo.enq = {
	map : {},
	timeline : {}
};

// 
// 
// Enquête
// 
// 

oo.enq.init = function(){

	oo.filt.on( oo.filt.events.init, function( event, data ){
		oo.log("[oo.enq.init]");

		oo.enq.map.update( data.objects );
		oo.enq.timeline.update( data.objects );

		oo.log('[oo.enq]', oo.enq)
	});
	// change
	// oo.enq.map.update( oo.filt.data );
	//

}

// 
// 
// Plugin filters
// 
// 

oo.filt.cross.extent = function( item, ExtentObject ){
	// if item is in ExtentObject
    //	return true
    return false;
}

oo.filt.cross.extent = function( item, ExtentObject ){
	// if item is in ExtentObject
    //	return true
    return false;
}

// 
// 
// Map
// 
// 

oo.enq.map.init = function(){
	
	oo.filt.on( oo.filt.events.change, function(e, filters){
		oo.log(e, filters, oo.filt.data );
	});

};

oo.enq.map.update = function ( objects ){

	oo.enq.map.data = { type: "FeatureCollection", features:[]};

	for( var i in objects ){
		oo.enq.map.data.features.push( objects[i].coordinates );
	}

	// Viz

	oo.enq.map.map = mapbox.map('map');
    oo.enq.map.map.addLayer(mapbox.layer().id('fumoseaffabulazioni.map-80sq0fh2'));

    layer = oo.enq.map.d3layer().data(oo.enq.map.data);
	oo.enq.map.map.addLayer(layer);
	oo.enq.map.map.extent(layer.extent());

	oo.enq.map.map.ui.zoomer.add();
	
	oo.enq.map.map.addCallback('panned', function(map, panOffset) {
		oo.filt.trigger( oo.filt.events.replace, {'extent': map.extent()} );
	});

	oo.enq.map.map.addCallback('zoomed', function(map, zoomOffset) {
		setTimeout( function() {
    		oo.filt.trigger( oo.filt.events.replace, {'extent': map.extent()} );
    	}, 1000 );
	});

	oo.log('[oo.enq.map]', oo.enq.map)	

}

oo.enq.map.d3layer = function() {

    var f = {}, bounds, feature, collection;

    var div = d3.select(document.body).append("div").attr('class', 'd3_layer'),
        svg = div.append('svg'),
          g = svg.append("g");

    f.parent = div.node();

    f.project = function(x) {
      var point = f.map.locationPoint({ lat: x[1], lon: x[0] });
      return [point.x, point.y];
    };

    var first = true;
    f.draw = function() {
      first && svg.attr("width", f.map.dimensions.x)
          .attr("height", f.map.dimensions.y*2)
          .style("margin-left", "0px")
          .style("margin-top", "0px") && (first = false);

      path = d3.geo.path().projection(f.project);

      feature.attr("d", path)
      	.attr('lon', function(d, i) { return collection.features[i].geometry.coordinates[0]; })
      	.attr('lat', function(d, i) { return collection.features[i].geometry.coordinates[1]; });
    };

    f.data = function(x) {
        collection = x;
        bounds = d3.geo.bounds(collection);
        feature = g.selectAll("path")
            .data(collection.features)
            .enter().append("path")
            .on("click", function(d,i) {
            	f.map.center({
            		'lat' : d3.select(this).attr('lat'),
            		'lon' : d3.select(this).attr('lon')
            	}, true);
				setTimeout( function() {
	        		oo.filt.trigger( oo.filt.events.replace, {'extent': f.map.extent()} );
	        	}, 1000 );
            });

        return f;
    };

    f.extent = function() {
        return new MM.Extent(
            new MM.Location(bounds[0][1], bounds[0][0]),
            new MM.Location(bounds[1][1], bounds[1][0]));
    };

    return f;
};

// 
// 
// Timeline
// 
// 

oo.enq.timeline.init = function(){

	oo.filt.on( oo.filt.events.change, function(e, filters){
		oo.log(e, filters, oo.filt.data );
	});
	
};

oo.enq.timeline.update = function( objects ){

	var format = d3.time.format("%Y-%m-%d");

	oo.enq.timeline.data = d3.range(objects.length).map(function(i) {
		return {
			x: format.parse(objects[i].times[0].time),
			y: Math.floor(Math.random()*5)
		};
	});

	var width = $('#map').width(),
		height = $('#map').height(),
		margin = {top: 20, right: 10};

	var minX = d3.min(oo.enq.timeline.data, function (d) { return d.x }),
		maxX = d3.max(oo.enq.timeline.data, function (d) { return d.x }),
		minY = d3.min(oo.enq.timeline.data, function (d) { return d.y }),
		maxY = d3.max(oo.enq.timeline.data, function (d) { return d.y }),
		scaleX = d3.time.scale().domain([minX, maxX]).range([ 0, width - margin.right*2 ]),
		scaleY = d3.scale.linear().domain([minY, maxY]).range([0, 20]); // Set a proper height

	var container = d3.select('#timeline').append('svg');
	
	oo.enq.timeline.brush = container.append('g');
	oo.enq.timeline.circles = container.append('g');

	d3.selectAll('#timeline g').attr("transform", "translate(" + margin.right + "," + margin.top + ")");

	oo.enq.timeline.circles.selectAll(".dot")
		.data(oo.enq.timeline.data)
		.enter().append("circle")
		.attr('class', 'dot')
		.attr("cx", function(d) { return scaleX(d.x); })
		.attr("cy", function(d) { return scaleY(d.y); })
		.attr("data-time", function(d) { return d.x; })
		.attr("r", 4);

	// Circles behavior

	$('#timeline').on('click', 'circle', function() {

		var domain = scaleX.domain();
		var oneTenthDomain = ( domain[1] - domain[0] ) / 8;
		var extent = brushObj.extent();
		var circleTime = new Date( $(this).attr('data-time') );
		var left = circleTime.getTime() - oneTenthDomain / 2;
		var right = circleTime.getTime() + oneTenthDomain / 2;

		oo.log('domain', domain)
		oo.log('oneTenthDomain', oneTenthDomain)
		oo.log('extent', extent)
		oo.log('circleTime', circleTime)
		oo.log('left', left, 'right', right)

		brushObj.extent([left, right]);
		oo.enq.timeline.brush.call(brushObj);

	});

	// Brush
	
	var brushObj = d3.svg.brush()
		.x(scaleX)
		.extent(scaleX.domain())
		.on("brushend", brushMove);

	oo.enq.timeline.brush.attr("class", "x brush")
		.call(brushObj)
		.selectAll("rect")
		.attr("y", - margin.top - 1 )
		.attr("height", $('#timeline').height() +1);

	d3.select('rect.extent').attr("class", "extent transition");

	function brushMove() {

		// this returns a period of time
		// To check

		var b = brushObj.empty() ? scaleX.domain() : brushObj.extent();
		oo.filt.trigger( oo.filt.events.replace, {'period': b } );

	}

	oo.log('[oo.enq.timeline]', oo.enq.timeline)

};



