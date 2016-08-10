module TimeHelper
  extend ActiveSupport::Concern

  included do
    before_action :format_time, only: :create
  end

  private

  def format_time
    resource = controller_name.singularize.to_sym
    begin
      params[resource][:created_at] = Time.parse(params[resource][:created_at]).utc.to_f
    rescue
      params[resource][:created_at] = Time.at(params[resource][:created_at].to_f).utc
    end
  end
end
