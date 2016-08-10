module Showable
  extend ActiveSupport::Concern

  included do
    before_action :set_resource, only: :show
  end

  def show
    render json: @resource
  end

  private

  def set_resource
    @resource = controller_name.classify.constantize.find(params[:id])
  end
end
