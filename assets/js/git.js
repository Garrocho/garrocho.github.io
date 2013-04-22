jQuery.getJsonRepos = function(nome, callback) {
  jQuery.getJSON('https://api.github.com/users/'+nome+'/repos?callback=?',callback)
}

jQuery.fn.carregarRepositorios = function(nome) {
  this.html('</br> <center> <img src="assets/img/githubcat.gif" height="64" width="64"> </center> </br> <center> <span>Carregando os Projetos de <strong>' + nome + '</strong> do GitHub...</span> </center>');

  var target = this;
  $.getJsonRepos(nome, function(data) {
  var repos = data.data;
  ordenarPorWatchers(repos);

  var list = $('<dl>');
  target.empty().append(list);
  $(repos).each(function() {
	if (this.name != (nome.toLowerCase()+'.github.com') && this.name != 'TSI') {
    list.append('<dt><a href="'+ (this.homepage?this.homepage:this.html_url) +'">' + this.name + '</a> <em>'+(this.language?('('+this.language+')'):'')+'</em></dt>');
    list.append('<dd>' + this.description + '</dd>');
    list.append('<dd><em>Tamanho: '+(this.size<1000?(this.size+' kB'):(Math.round((this.size/1000)*100)/100+' MB'))+' &mdash; Stars: <a href="'+ this.url.replace("api.","").replace("repos/","")+'/stargazers">'+this.watchers+'</a> &mdash; Forks: <a href="'+ this.url.replace("api.","").replace("repos/","")+'/network/members">'+this.forks+'</a> </em></dd>');
    list.append('<dd><a href="'+this.url.replace("api.","").replace("repos/","")+'#readme">Readme</a> &mdash; <a href="' + this.url.replace("api.","").replace("repos/","")+'/zipball/master">Download</a> </dd>');
    list.append('<dd><br/></dd>');
	  }
  });   
});

function ordenarPorWatchers(repos) {
  repos.sort(function(a,b) {
  return (b.watchers - a.watchers) ;
  });
}
};