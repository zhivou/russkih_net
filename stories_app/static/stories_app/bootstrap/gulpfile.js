const gulp = require('gulp');
const browserSync = require('browser-sync').create();
const sass = require('gulp-sass');

// Compile Sass & Inject Into Browser
gulp.task('sass', function(){
  return gulp.src(['node_modules/bootstrap/scss/bootstrap.scss', 'src/scss/*.scss'])
    .pipe(sass()) //using plugin which compile the func
    .pipe(gulp.dest("src/css")) // compiled sass -> css and put it into folder
  //  .pipe(browserSync.stream());
});

// Move JS Files to src/js
gulp.task('js', function(){
  return gulp.src(['node_modules/bootstrap/dist/js/bootstrap.min.js','node_modules/jquery/dist/jquery.min.js','node_modules/popper.js/dist/umd/popper.min.js'])
    .pipe(gulp.dest("src/js"))
  //  .pipe(browserSync.stream());
});

// Watch Sass & Server
// If i understood it correctly it will watch for any chnges in bootstrap/scss and in cutom sass folder to apply it right after
// the changes were made! Oh and also it will happen in case of any html files changes in src foulder

gulp.task('serve', ['sass'], function(){
  browserSync.init({
    server: "./src" //defining the server folder
  });
  gulp.watch(['node_modules/bootstrap/scss/bootstrap.scss', 'src/scss/*.scss'], ['sass']);
//  gulp.watch("src/*.html").on('change', browserSync.reload);
});

//Move Fonts Folder to src/fonts
gulp.task('fonts', function(){
  return gulp.src('node_modules/font-awesome/fonts/*')
    .pipe(gulp.dest("src/fonts"));
});

//Move Font Awesome CSS to src/css
gulp.task('fa', function(){
  return gulp.src('node_modules/font-awesome/css/font-awesome.min.css')
    .pipe(gulp.dest("src/css"));
});

// this will start all tasks by jsut using gulp command in cmd. Only on thing is strange here why is doesn't call sass may be because
//it is just becasuse the serc would resive the [sass] into it ?? Could be!
gulp.task('default', ['js','serve','fa','fonts']);
