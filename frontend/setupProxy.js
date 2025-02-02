const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(
    '/api',
    createProxyMiddleware({
      target: `http://${process.env.REACT_APP_BACKEND}:3001`,
      changeOrigin: true,
    })
  );
};
