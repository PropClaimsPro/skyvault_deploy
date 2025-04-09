  spec:
    name: skyvault
    region: nyc
    services:
      - name: skyvault-service
        environment_slug: python
        git:
          branch: main
          repo_clone_url: https://github.com/your-username/skyvault-deploy
        build_command: pip install -r requirements.txt
        run_command: gunicorn --worker-tmp-dir /dev/shm wsgi:app
        http_port: 8080
        instance_count: 1
        instance_size_slug: professional-xs
        routes:
          - path: /
