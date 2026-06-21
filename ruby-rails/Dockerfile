FROM ruby:3.3-alpine
WORKDIR /app
COPY Gemfile Gemfile.lock ./
RUN bundle install || true
COPY . .
EXPOSE 3000
CMD ["rails", "server", "-b", "0.0.0.0"]
