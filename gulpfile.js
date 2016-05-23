
gulp = require('gulp');

var plugins = require('gulp-load-plugins')();
var exec = require('child_process').exec;

var source = './pelican-kiwi-theme/src/';
var source_blog = 'src/';
var destination = './dest/';
var content = './content';

/** CSS PART */
gulp.task('css', function() {
    return gulp.src(source+"css/main.scss")
    .pipe(plugins.sass())
    .pipe(plugins.csscomb())
    .pipe(plugins.autoprefixer())
    .pipe(plugins.csso())
    .pipe(plugins.rename({
        suffix: '.min'
    }))
    .pipe(gulp.dest(destination+"kiwi/static/css/"));
});

/** JS PART */
gulp.task('js', function(){
    return gulp.src(source+"js/*")
    .pipe(plugins.uglify())
    .pipe(plugins.concat('global.min.js'))
    .pipe(gulp.dest(destination+"kiwi/static/js/"));
});

/** IMG PART */
gulp.task('img', function() {
    return gulp.src(source+"images/*.{png,jpg,jpeg,gif,svg}")
    .pipe(plugins.imagemin())
    .pipe(gulp.dest(destination+"kiwi/static/img/"));
});

gulp.task('ico', function() {
    return gulp.src(source+"images/*.ico")
    .pipe(gulp.dest(destination+"kiwi/static/img/"));
});

/** HTML PART */
gulp.task('html', function() {
    return gulp.src(source+"html/*html")
    .pipe(gulp.dest(destination+"kiwi/templates/"));
});

/** WATCH PART */
gulp.task('watch', function() {
    gulp.watch(source+"css/*.less", ['css']);
    gulp.watch(source+"html/*.html", ['html']);
    gulp.watch(source+"images/*.{png,jpg,jpeg,gif,svg,ico}", ['img', 'ico']);
    gulp.watch(source+"js/*", ['js']);
});

gulp.task('publish', function(cb) {
    exec('make publish && ghp-import output && git push origin gh-pages', function (err, stdout, stderr) {
        console.log(stdout);
        console.log(stderr);
        cb(err);
  });
});

gulp.task('cvCSS', function(cb) {
    return gulp.src(source_blog+"cv/cv.scss")
    .pipe(plugins.sass())
    .pipe(plugins.csscomb())
    .pipe(plugins.autoprefixer())
    .pipe(plugins.csso())
    .pipe(plugins.rename({
        suffix: '.min'
    }))
    .pipe(gulp.dest(content+"/cv/"));
});

gulp.task('content', function() {
    return gulp.src(source_blog+"/content/*")
    .pipe(gulp.dest(content));
});

gulp.task('user-images', function() {
  return gulp.src(source_blog+"/images/*.{png,jpg,jpeg,gif,svg}")
  .pipe(plugins.imagemin())
  .pipe(gulp.dest(content+"/images/"));
});

gulp.task('cvHTML', function() {
    return gulp.src(source_blog+"cv/*.{html,woff2}")
    .pipe(gulp.dest(content+"/cv/"));
});

gulp.task('cvImg', function() {
  return gulp.src(source_blog+"cv/*.{png,jpg,jpeg,gif,svg}")
  .pipe(plugins.imagemin())
  .pipe(gulp.dest(content+"/cv/"));
});

gulp.task('cv', ['cvCSS', 'cvHTML', 'cvImg'])

gulp.task('build', ['css', 'js', 'html', 'img', 'ico', 'content', 'user-images', 'cv']);
gulp.task('default', ['build']);
