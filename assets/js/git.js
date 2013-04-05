jQuery.getJsonRepos = function(nome, callback) {
jQuery.getJSON('https://api.github.com/users/'+nome+'/repos?callback=?',callback)
}

jQuery.fn.carregarRepositorios = function(nome) {
this.html("<span>Consultando os Repositorios de " + nome +"...</span>");

var target = this;
$.getJsonRepos(nome, function(data) {
var repos = data.data;
ordenarPorFork(repos);  

var list = $('<dl/>');
target.empty().append(list);
$(repos).each(function() {
if (this.name != (nome.toLowerCase()+'.github.com')) {
list.append('<dt><a href="'+ (this.homepage?this.homepage:this.html_url) +'">' + this.name + '</a> <em>'+(this.language?('('+this.language+')'):'')+'</em></dt>');
list.append('<dd>' + this.description +'</dd>');
list.append('<dd><em>Tamanho: '+(this.size<1000?(this.size+' kB'):(Math.round((this.size/1000)*100)/100+' MB'))+' - Watchers: '+this.watchers+' - Forks: '+this.forks+' </em></dd>');
list.append('<dd><br/></dd>');
}
});   
});

function ordenarPorFork(repos) {
  repos.sort(function(a,b) {
    return b.forks - a.forks;
  });
  }
};