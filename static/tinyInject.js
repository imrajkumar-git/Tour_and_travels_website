var script = document.createElement('script');
script.type = 'text/javascript';
script.src = "https://cdn.tiny.cloud/1/u6d6drp5f5nqzvqu6eujg1dnek4vrscdre339fvjpf0ik7bw/tinymce/5/tinymce.min.js"
document.head.appendChild(script);

script.onload = function(){
	tinymce.init({
		selector: 'textarea', 
		images_upload_url: '/upload_image/', 
		
		height: 456,
		plugins: [
	  		'advlist autolink link image lists charmap print preview hr anchor pagebreak',
		  	'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking',
		  	'table emoticons template paste help maxchars'
		],
		toolbar: 'fullscreen | undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | ' +
		  	'bullist numlist outdent indent | link image | print preview media fullpage | ' +
		  	'forecolor backcolor emoticons | uploadimage help ',	
		paste_data_images: true,
		menu: {
	  		favs: {title: 'My Favorites', items: 'code visualaid | searchreplace | emoticons'}
		},
		menubar: 'favs file edit view insert format tools table help',
		content_css: 'css/content.css'
	})
}