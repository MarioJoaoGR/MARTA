# Keep the official Ruby 3.2 and its nine working bundles. Ruby 3.3 is
# installed separately for Hanami; no benchmark Ruby source is changed here.
FROM dungxg502/xrepotest-ruby@sha256:e7e857ff5c73345a9492a5352a52262da9796a3cb29c5f18053e0be1e8b6924d AS ruby-build
RUN mkdir -p /tmp/xrepo-ruby-build && cd /tmp/xrepo-ruby-build \
    && curl --fail --location --retry 3 -o ruby.tar.gz https://cache.ruby-lang.org/pub/ruby/3.3/ruby-3.3.10.tar.gz \
    && echo 'b555baa467a306cfc8e6c6ed24d0d27b27e9a1bed1d91d95509859eac6b0e928  ruby.tar.gz' | sha256sum -c - \
    && tar -xzf ruby.tar.gz && cd ruby-3.3.10 \
    && ./configure --prefix=/opt/xrepo/ruby33 --disable-install-doc --disable-yjit > /tmp/configure.log 2>&1 \
    && make -j4 > /tmp/make.log 2>&1 && make install > /tmp/install.log 2>&1 \
    || { tail -50 /tmp/configure.log /tmp/make.log /tmp/install.log; exit 1; }

FROM dungxg502/xrepotest-ruby@sha256:e7e857ff5c73345a9492a5352a52262da9796a3cb29c5f18053e0be1e8b6924d
COPY --from=ruby-build /opt/xrepo/ruby33 /opt/xrepo/ruby33
RUN env -u GEM_HOME -u GEM_PATH /opt/xrepo/ruby33/bin/ruby -e 'require "openssl"; require "yaml"; require "zlib"; puts RUBY_DESCRIPTION'
COPY prepare_hanami.py /opt/xrepo/recipe/
COPY locks/hanami.lock /opt/xrepo/recipe/locks/hanami.lock
RUN python3 -B /opt/xrepo/recipe/prepare_hanami.py
COPY prepare_mutation.py finish.py /opt/xrepo/recipe/
COPY locks/ /opt/xrepo/recipe/locks/
RUN python3 -B /opt/xrepo/recipe/prepare_mutation.py capybara dotenv grape hanami hashie httparty pundit rom rspec-core shoryuken \
    && python3 -B /opt/xrepo/recipe/finish.py
COPY repair_evaluator.py /opt/xrepo/recipe/
RUN python3 -B /opt/xrepo/recipe/repair_evaluator.py
