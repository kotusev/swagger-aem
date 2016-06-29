require_relative 'spec_helper'

describe 'Package' do
  before do
    init_client
    @crx = SwaggerAemClient::CrxApi.new

    # ensure package does not exist
    data, status_code, headers = @crx.post_package_service_json_with_http_info(
      name = 'somepackagegroup/somepackage-1.2.3.zip',
      cmd = 'delete'
    )
    expect(status_code).to eq(200)

    # create package
    data, status_code, headers = @crx.post_package_service_json_with_http_info(
      name = 'somepackage',
      cmd = 'create',
      {
        :group_name => 'somepackagegroup',
        :package_name => 'somepackage',
        :package_version => '1.2.3',
        :charset => 'utf-8'
      }
    )
    expect(status_code).to eq(200)
  end

  after do
  end

  describe 'test package build install replicate' do

    it 'should succeed' do

      # build package
      data, status_code, headers = @crx.post_package_service_json_with_http_info(
        name = 'somepackagegroup/somepackage-1.2.3.zip',
        cmd = 'build'
      )
      expect(status_code).to eq(200)

      # install package
      data, status_code, headers = @crx.post_package_service_json_with_http_info(
        name = 'somepackagegroup/somepackage-1.2.3.zip',
        cmd = 'install'
      )
      expect(status_code).to eq(200)

      # replicate package
      data, status_code, headers = @crx.post_package_service_json_with_http_info(
        name = 'somepackagegroup/somepackage-1.2.3.zip',
        cmd = 'replicate'
      )
      expect(status_code).to eq(200)

    end

  end

  describe 'test package update' do

    it 'should succeed' do

      # update package
      data, status_code, headers = @crx.post_package_update_with_http_info(
        groupName = 'somepackagegroup',
        packageName = 'somepackage',
        version = '1.2.3',
        path = '/etc/packages/somepackagegroup/somepackage-1.2.3.zip',
        {
          :charset => 'utf-8'
        }
      )
      expect(status_code).to eq(200)

    end

  end

end