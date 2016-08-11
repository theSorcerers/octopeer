# This module allows a resource to be created. To use this module the controller
# must rename the `resource_params` method to `parameters`.
#
# For example:
#
# class Api::UsersController < ApplicationController
#   private
#
#   def parameters
#     params.require(:user).permit(:username)
#   end
# end

module Createable
  extend ActiveSupport::Concern

  def create
    @resource = controller_name.classify.constantize.new(parameters)

    if @resource.save
      render json: @resource, status: :created
    else
      render json: @resource.errors, status: :unprocessable_entity
    end
  end
end
