path = require('path');
const dest_templates_root = path.resolve(__dirname, '../serverside/app/app/templates/')
const dest_static_root = path.resolve(__dirname, '../serverside/app/app/static/')

module.exports = {
    html: {
        src: {
            entry: ['src/pug/**/*.pug'],
            ignore: ['!src/pug/**/_*']
        },
        dest: path.resolve(dest_templates_root)
    },
    css: {
        src: {
            entry: ['src/scss/**/*.sass', 'src/scss/**/*.scss', `src/scss/**/*.css`],
            ignore: ['!src/scss/**/_*']
        },
        dest: path.resolve(dest_static_root, 'css/')
    },
    js: {
        src: {
            target: ['src/ts/**/*.vue', 'src/ts/**/*.ts', 'src/ts/**/*.js'],
            entry: {
                'main': path.resolve(__dirname, 'src/ts/main.ts')
            },
        },
        dest: path.resolve(dest_static_root, 'js/')
    }
}