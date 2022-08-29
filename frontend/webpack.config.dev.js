#!/usr/bin/env node

const os = require('os');
const path = require('path')
const TerserPlugin = require('terser-webpack-plugin');
const paths = require('./paths');


module.exports = {
    mode: 'development',
    target: ['web'],
    entry: paths.js.src.entry,
    output: {
        path: paths.js.dest,
        filename: path.join('[name].bundle.js'),
    },
    resolve: { extensions: ['.ts', '.js'],},
    module: {
        rules: [{
            test: /\.(ts|js)$/,
            exclude: /node_modules/,
            use: [
                'babel-loader', // オプションは babel.config.json / .babelrc で指定する
                'ts-loader'     // tsconfig.json も参照
            ]}
        ]
    },
    optimization: {
        minimize: true,
        minimizer: [
            new TerserPlugin({
                parallel: os.cpus().length - 1,
                extractComments: false,
                terserOptions: {
                    compress: {
                        drop_console: true, // console.log削除
                    },
                },
            }),
        ],
    }
};