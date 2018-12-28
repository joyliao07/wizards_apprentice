var inputs = document.querySelectorAll( '.upload' );
Array.prototype.forEach.call( inputs, function( input )
{
	var label	 = input.nextElementSibling.firstChild,
		labelVal = label.innerHTML;

	input.addEventListener( 'change', function( e )
	{
		var fileName = '';
		if( this.files && this.files.length > 1 )
			fileName = ( this.getAttribute( 'data-multiple-caption' ) || '' ).replace( '{count}', this.files.length );
		else
			fileName = e.target.value.split( '\\' ).pop();

		if( fileName )
			label.innerHTML = '<i class="fas fa-upload"></i> ' + fileName;
		else
			label.innerHTML = '<i class="fas fa-upload"></i> ' + labelVal;
	});
});
