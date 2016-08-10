module Createable
  extend ActiveSupport::Concern

  def create
    @resource = controller_name.classify.constantize.new(resource_params)

    if @resource.save
      render json: @resource, status: :created
    else
      render json: @resource.errors, status: :unprocessable_entity
    end
  end

  private

  def resource_params
    send (controller_name.singularize + '_params').to_sym
  end
end
