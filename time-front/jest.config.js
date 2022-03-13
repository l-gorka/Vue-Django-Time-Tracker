module.exports = {
  preset: '@vue/cli-plugin-unit-jest',
  setupFiles: ["<rootDir>/tests/unit/index.js"],
  moduleNameMapper: {
    '\\.(css|less|sass|scss)$': 'identity-obj-proxy',
  },
}
