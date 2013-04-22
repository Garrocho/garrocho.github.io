jQuery.getJsonRepos = function(nome, callback) {
  jQuery.getJSON('https://api.github.com/users/'+nome+'/repos?callback=?',callback)
}

jQuery.fn.carregarRepositorios = function(nome) {
  this.html('<center> <i class="icon-spinner icon-spin icon-3x"></i> </center> </br> <center> <span>Carregando os Projetos de <strong>' + nome + '</strong> do GitHub...</span> </center>');

  var target = this;
  $.getJsonRepos(nome, function(data) {
  var repos = data.data;
  ordenarPorWatchers(repos);

  var list = $('<dl>');
  target.empty().append(list);
  $(repos).each(function() {
	if (this.name != (nome.toLowerCase()+'.github.com') && this.name != 'TSI') {
    list.append('<div class="well well-transparent"> <a href="'+ (this.homepage?this.homepage:this.html_url) +'"> ' + this.name + '</a> <em> '+(this.language?('('+this.language+')'):'')+' </em> <div class="pull-right"> <a class="btn" href="'+ this.url.replace("api.","").replace("repos/","")+'/stargazers" ><i class="icon-star" title="Stars"></i> '+this.watchers+'</a> <a class="btn" href="'+ this.url.replace("api.","").replace("repos/","")+'/network/members"><i class="icon-group" title="Forks"></i> '+this.forks+'</a> <a class="btn" href="'+this.url.replace("api.","").replace("repos/","")+'#readme"><i class="icon-book" title="Readme"></i> Readme</a> <a class="btn" href="' + this.url.replace("api.","").replace("repos/","")+'/zipball/master"><i class="icon-download-alt" title="Download"> Download</i></a> </div> <p>' + this.description + '</p> </div>');
    }
  });   
});

function ordenarPorWatchers(repos) {
  repos.sort(function(a,b) {
  return (b.watchers - a.watchers) ;
  });
}
};